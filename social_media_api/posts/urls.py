from rest_framework.routers import DefaultRouter
from .views import PostView, CommentView, FeedView, like_post, unlike_post
from django.urls import path, include

router = DefaultRouter()
router.register(r'post', PostView)
router.register(r'comment', CommentView)


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='posts-feed'),

    # Like URLs
    path('posts/<int:pk>/like/', like_post, name='like-post'),
    path('posts/<int:pk>/unlike/', unlike_post, name='unlike-post'),
]