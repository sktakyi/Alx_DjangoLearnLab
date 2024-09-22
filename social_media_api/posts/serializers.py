from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth import get_user_model

# Getting the CustomUser model
User = get_user_model()

# User serializer for the custom user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'followers']


# Comment serializer
class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['post', 'author', 'content', 'created_at', 'updated_at']    

    # Validating data to ensure the author of the comment
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)
        
# Post serializer class
class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True) # a post can have many comments and vice versa

    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'created_at', 'updated_at', 'comments']

        # Validating data to ensure the creator of the post
        def create(self, validated_data):
            validated_data['author'] = self.context['request'].user
            return super().create(validated_data)


# Like serializer class
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'post']
        