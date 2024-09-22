from rest_framework import serializers
from .models import Notification
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer

# Notification model
class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()  # Use the string representation of the user
    target = serializers.SerializerMethodField()  # Custom field to handle GenericForeignKey

    class Meta:
        model = Notification
        fields = ['id', 'recipient','actor', 'verb', 'target', 'timestamp', 'is_read']


    def get_target(self, obj):
        if isinstance(obj.target, Post):
            return PostSerializer(obj.target).data
        return None