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
    post = get_object_or_404(Post, pk=post_id)  # Check if the post exists
    user = request.user

    # Check if the post is already liked by the user
    if Like.objects.filter(user=user, post=post).exists():
        return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a Like object
    Like.objects.create(user=user, post=post)

    # Generate a notification for the post author
    Notification.objects.create(
        recipient=post.author,
        actor=user,
        verb='liked your post',
        target=post
    )

    return Response({'message': f'You liked {post.title}'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, post_id):
    """View to handle unliking a post."""
    post = get_object_or_404(Post, pk=post_id)  # Check if the post exists
    user = request.user

    # Check if the post is liked by the user
    try:
        like = Like.objects.get(user=user, post=post)
        like.delete()  # Unlike the post
        return Response({'message': f'You unliked {post.title}'}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({'message': 'You have not liked this post yet.'}, status=status.HTTP_400_BAD_REQUEST)
