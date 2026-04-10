# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .services import fetch_github_repo, fetch_stackoverflow_related
from django.shortcuts import get_object_or_404
from .models import Comment, Post, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer
from .permissions import IsOwnerOrAdmin

class Categories(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # require authentication and read only

    def get(self, request):
        categories = Category.objects.all().order_by("name")
        return Response(CategorySerializer(categories, many=True).data)

class Posts(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]  # require authentication

    def get(self, request):
        posts = Post.objects.select_related("author", "category").all().order_by("-created_at")  # optimized query
        return Response(PostSerializer(posts, many=True).data)  # return serialized list

    def post(self, request):
        serializer = PostSerializer(data=request.data)  # validate incoming data
        if serializer.is_valid():
            serializer.save(author=request.user)  # attach logged in user as author
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrAdmin]  # auth + ownership required

    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)  # fetch post or 404
        serialized = PostSerializer(post).data 

        # attach GitHub repo metadata if repo_url exists
        if post.repo_url:
            serialized["repo_metadata"] = fetch_github_repo(post.repo_url)

        # attach related StackOverflow results
        serialized["related_stackoverflow"] = fetch_stackoverflow_related(post.title)

        return Response(serialized)

    def put(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        self.check_object_permissions(request, post)  # enforce owner check
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()  # update post
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        self.check_object_permissions(request, post)
        post.delete()  # delete post
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostComments(APIView):
    permission_classes = [IsAuthenticated]  # must be logged in to comment

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, post=post)  # attach user and post
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentDetail(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]  # protect comment updates

    def put(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        self.check_object_permissions(request, comment)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()  # update comment
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        self.check_object_permissions(request, comment)
        comment.delete()  # delete comment
        return Response(status=status.HTTP_204_NO_CONTENT)
