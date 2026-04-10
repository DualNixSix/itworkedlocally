# serializers.py

from rest_framework import serializers
from .models import Category, Post, Comment

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]  # expose category id and name

class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)  # show username instead of raw FK

    class Meta:
        model = Comment
        fields = ["id", "post", "body", "author", "author_username", "created_at"]
        read_only_fields = ["author", "post", "created_at"]  # prevent client from overriding these

class PostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)  # include readable author name
    comments = CommentSerializer(many=True, read_only=True)  # nested comments in post response
    category_name = serializers.CharField(source="category.name", read_only=True)  # include readable category name

    class Meta:
        model = Post
        fields = [
            "id","category","category_name","title","author","author_username",
            "created_at","updated_at","body","repo_url","comments"
        ]
        read_only_fields = ["author", "created_at", "updated_at"]  # protect system managed fields
