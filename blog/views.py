# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostDetail(DetailView):
    model = Post

class PostList(ListView):
    model = Post
    ordering = '-pk'
