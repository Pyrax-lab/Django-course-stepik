from django.shortcuts import render

from rest_framework import generics 
# Create your views here.
from rest_framework.response import Response
from blog.models import Post 
from .serializers import PostSerializer

from rest_framework.views import APIView # данный класс стоит во главе все классов

# get  - вызывается когда мы хотим получить какуето инофрмацию 
# post - вызывается когда мы хотим сохранить инфу в базе данных


# 1. Самый простой класс представления наследуется от APIView и при get-запросе отдаёт такой json {"title" : "simple get api"}
class PostList(APIView):
    def get(self, request):
        return Response({"title" : "simple get api"})
# 2. Класс представления которые отправляет в json формате список из всех постов модели Post
class PostList(APIView):
    def get(self, request):
        return Response({"posts":Post.objects.all().values()})

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer