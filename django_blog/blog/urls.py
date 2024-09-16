from django.urls import path
from .views import (
    UserLoginView, UserLogoutView, register, profile_view,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    add_comment, edit_comment, delete_comment
)

urlpatterns = [
    # Authentication-related paths
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile_view, name='profile'),
    
    # Post-related paths
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

    # Comment-related paths
    path('posts/<int:post_id>/comments/new/', add_comment, name='add_comment'),
    path('comments/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]