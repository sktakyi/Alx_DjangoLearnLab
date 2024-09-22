from django.shortcuts import render
from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from .models import Post, Comment, Like
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework
from rest_framework.response import Response
from notifications.models import Notification


# Create Views for CRUD Operations

# Custom permission to only allow authors of an object to edit or delete it.
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allowed to the author of the post/comment
        return obj.author == request.user

    

# Post View
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['title']
    search_fields = ['title', 'content']
    pagination_class = PageNumberPagination


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Comment view
class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        comment = serializer.save(author=self.request.user)
        post = comment.post

        if post.author != self.request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=self.request.user,
                verb= f'commented on your post {post.title}',
                target = post
            )

# Feed View 
class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get the list of all users the current user is following
        following_users = self.request.user.following.all()

        # Retrieve post from the users the current user is following, ordering by most recent date created
        return Post.objects.filter(author__in=following_users).order_by("-created_at")


# Post liking View
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient = post.author,
                actor = request.user,
                verb = f'liked your post {post.title}',
                target = post
            )
            return Response({'message': 'Post liked successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'You have already liked this post'}, status=status.HTTP_400_BAD_REQUEST)
    except Post.DoesNotExist:
        return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)   
    


# Unlike post if it exist or not liked
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        like = Like.objects.get(user= request.user, post=post)
        like.delete()
        return Response({'message': 'Post unliked successfully'}, status=status.HTTP_200_OK)
    
    except (Post.DoesNotExist, Like.DoesNotExist):
        return Response({'message': "You haven't liked this post"}, status=status.HTTP_404_NOT_FOUND)