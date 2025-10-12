from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet
from .views import FeedListView

router = DefaultRouter()
router.register('notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]
