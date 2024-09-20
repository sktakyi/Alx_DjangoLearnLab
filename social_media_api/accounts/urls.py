from django.urls import path
from .views import RegisterAPIView, LoginAPIView, ProfileAPIView, follow_user, unfollow_user

urlpatterns = [
    # Account URLS
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),

    # Follow/ UnFollow URLS
    path('follow/<int:user_id>/', follow_user, name='follow-user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow-user'),
]