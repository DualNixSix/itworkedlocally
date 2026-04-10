# app urls.py

from django.urls import path
from .views import Posts, PostDetail, PostComments, CommentDetail, Categories

urlpatterns = [
    path("categories/", Categories.as_view()),  # list categories
    path("posts/", Posts.as_view()),  # list and create posts
    path("posts/<int:post_id>/", PostDetail.as_view()),  # retrieve, update, delete single post
    path("posts/<int:post_id>/comments/", PostComments.as_view()),  # create comment for a post
    path("comments/<int:comment_id>/", CommentDetail.as_view()),  # update or delete comment
]