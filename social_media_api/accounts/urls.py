from django.urls import path
from .views import RegisterView, LoginView, FollowUserView, UnfollowUserView, FollowersListView, FollowingListView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
    path('followers/<int:user_id>/', FollowersListView.as_view(), name='user-followers'),
    path('following/<int:user_id>/', FollowingListView.as_view(), name='user-following')

]
