from django.urls import path
from .views import UserFeedView, LikePostView, UnlikePostView

urlpatterns = [
    path('feed/', UserFeedView.as_view(), name='user_feed'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like_post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike_post'),
]