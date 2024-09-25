from rest_framework import viewsets, permissions, views
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification
from rest_framework.permissions import IsAuthenticated


# Viewset for Post Model
class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    queryset = Post.objects.all()  # Fetch all posts
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Handle the creation of a new post and add custom logic."""
        post = serializer.save(author=self.request.user)
        # Custom logic such as notifications can be added here
        return post

    # Add a custom action to retrieve posts from followed users
    def list_followed_posts(self, request):
        """Retrieve posts by users the current user follows."""
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=200)

# Viewset for Comment Model
class CommentViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing comment instances.
    """
    queryset = Comment.objects.all()  # Fetch all comments
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Handle the creation of a new comment."""
        post = get_object_or_404(Post, pk=self.request.data.get('post_id'))
        comment = serializer.save(user=self.request.user, post=post)
        # Add a notification to the post author when a comment is created
        Notification.objects.create(
            recipient=post.author,
            actor=self.request.user,
            verb='commented on your post',
            target=post
        )
        return comment

# Additional views for liking/unliking a post
class LikePostView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        """Like a post."""
        post = get_object_or_404(Post, pk=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if created:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post
            )
            return Response({'message': 'Post liked successfully'}, status=200)
        return Response({'message': 'You already liked this post'}, status=400)

class UnlikePostView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, post_id):
        """Unlike a post."""
        post = get_object_or_404(Post, pk=post_id)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'message': 'Post unliked successfully'}, status=200)
        except Like.DoesNotExist:
            return Response({'message': 'You have not liked this post yet'}, status=400)
