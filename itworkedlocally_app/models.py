# models.py

from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=250)  # category name

    def __str__(self):
        return self.name  # readable display

class Post(models.Model):
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)  # category relationship
    title = models.CharField(max_length=250)  # post title
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")  # post owner
    created_at = models.DateTimeField(auto_now_add=True)  # set on creation
    updated_at = models.DateTimeField(auto_now=True)  # auto update on save
    body = models.TextField()  # main content
    repo_url = models.URLField(blank=True)  # optional repository link

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)  # comment belongs to post
    body = models.TextField()  # comment text
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")  # comment owner
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"