# admin.py

from django.contrib import admin
from .models import Category, Post, Comment

admin.site.register(Category)  # enable admin management
admin.site.register(Post)
admin.site.register(Comment)