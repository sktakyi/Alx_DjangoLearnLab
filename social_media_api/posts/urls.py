from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView, FeedView, like_post, unlike_post
from django.urls import path, include
from .views import like_post, unlike_post


router = DefaultRouter()
router.register(r'post', PostView)
router.register(r'comment', CommentView)


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='posts-feed'),

    path('post/<int:pk>/like/', like_post, name='like_post'),
    path('post/<int:pk>/unlike/', unlike_post, name='unlike_post'), 
]