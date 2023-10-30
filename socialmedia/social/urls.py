from django.urls import path
from .views import SendFriendRequestView, AcceptFriendRequestView, FollowUserView, UnfollowUserView

app_name = 'social'

urlpatterns = [
    path('send_friend_request/<int:user_id>/', SendFriendRequestView.as_view(), name='send_friend_request'),
    path('accept_friend_request/<int:pk>/', AcceptFriendRequestView.as_view(), name='accept_friend_request'),
    path('follow_user/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow_user/<int:pk>/', UnfollowUserView.as_view(), name='unfollow_user'),
]
