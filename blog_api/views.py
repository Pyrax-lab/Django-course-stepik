from django.shortcuts import render

from rest_framework import generics 
# Create your views here.

from blog.models import Post 
from .serializers import PostSerializer

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer