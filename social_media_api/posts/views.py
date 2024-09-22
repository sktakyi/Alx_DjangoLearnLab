from django.shortcuts import get_object_or_404
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, post_id):
    """View to handle liking a post."""
    # Get the post object using get_object_or_404
    post = generics.get_object_or_404(Post, pk=post_id)
    
    # Create or get the Like object
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if created:
        # If it's a new like, create a notification
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )
        return Response({'message': f'You liked {post.title}'}, status=status.HTTP_200_OK)
    else:
        # If the like already exists
        return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, post_id):
    """View to handle unliking a post."""
    # Get the post object using get_object_or_404
    post = generics.get_object_or_404(Post, pk=post_id)
    
    # Try to find the like and delete it if it exists
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({'message': f'You unliked {post.title}'}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({'message': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)
