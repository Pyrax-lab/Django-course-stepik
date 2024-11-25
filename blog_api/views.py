from django.shortcuts import render

from rest_framework import generics, viewsets
# Create your views here.
from rest_framework.response import Response
from blog.models import Post 
from .serializers import PostSerializer

from rest_framework.views import APIView # данный класс стоит во главе все классов
from rest_framework.decorators import action


from taggit.models import Tag
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

# #4.  ListCreateAPIView содержит  в себе get и post 
# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# # 5. UpdateAPIView изменяет по put и patch запросу для него нужен отдельный url pk-для выборки по id чтобы изменять конкретный обьект
# class PostUpdate(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# # 6. Мы можемь создать класс унаследованный от RetrieveUpdateDestroyAPIView которые может получить изменить и удалить !ОДНУ! конкретную запись для неё нужно указать url <int:pk>
# class PostGetUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# ViewSet - заменяет все классы написанные выше и делает тоже саммое
class PostViewsets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    # переопределение queryset https://www.youtube.com/watch?v=Ur24Ms-MD5k&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=10 13:20

    
# ViewSet + action - создаём api для просмотра тегов
class PostViewsetsTags(PostViewsets):

    @action(methods=["get"], detail=False) # detail=True значит будет только 1 обьект
    def tags(self, request, pk=None): # теперь по адрессу http://127.0.0.1:8000/api/post/tags/, !!! имя в url tags = имя нашей функции !!!, теперь по этому адрессу получим все теги
        tag = Tag.objects.all()
        print(tag)
        return Response({'tags': [tg.name for tg in tag]})