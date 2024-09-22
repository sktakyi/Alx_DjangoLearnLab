from django.urls import path
from .views import NotificationListView

# Notification URLs
urlpatterns = [
    path('notifications/', NotificationListView.as_view(), name='notification-list'),
]