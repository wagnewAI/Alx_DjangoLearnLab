from django.urls import path, include
from .views import FeedListView
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet,  LikePostView, UnlikePostView
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
# urlpatterns = router.urls
urlpatterns = [
    path('feed/', FeedListView.as_view(), name='feed'),
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='post-like'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='post-unlike'),
]