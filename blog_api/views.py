from django.shortcuts import render

from rest_framework import generics, viewsets
# Create your views here.
from rest_framework.response import Response
from blog.models import Post 
from .serializers import PostSerializer

from rest_framework.views import APIView # данный класс стоит во главе все классов

# get  - вызывается когда мы хотим получить какуето инофрмацию 
# post - вызывается когда мы хотим сохранить инфу в базе данных


# 1. Самый простой класс представления наследуется от APIView и при get-запросе отдаёт такой json {"title" : "simple get api"}
# class PostList(APIView):
#     def get(self, request):
#         return Response({"title" : "simple get api"})


# # 2. Класс представления которые отправляет в json формате список из всех постов модели Post
# class PostList(APIView):
#     def get(self, request):
#         return Response({"posts":Post.objects.all().values()})

# 3. Данный класс реализует полученние данных с помошью get автоматически
# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#4.  ListCreateAPIView содержит  в себе get и post 
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# 5. UpdateAPIView изменяет по put и patch запросу для него нужен отдельный url pk-для выборки по id чтобы изменять конкретный обьект
class PostUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# 6. Мы можемь создать класс унаследованный от RetrieveUpdateDestroyAPIView которые может получить изменить и удалить !ОДНУ! конкретную запись для неё нужно указать url <int:pk>
class PostGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



# ViewSet - 
class PostViewsets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer