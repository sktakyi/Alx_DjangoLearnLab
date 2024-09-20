from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    token = serializers.CharField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_picture', 'token']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        user.token = token.key
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            data['token'] = token.key
            return data
        raise serializers.ValidationError("Invalid Credentials")
