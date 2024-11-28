from django.shortcuts import render


from blog.models import Post 
from .serializers import PostSerializer

from rest_framework.views import APIView # данный класс стоит во главе все классов
from rest_framework.decorators import action
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser


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


# #
# # 7 ViewSet - заменяет все классы написанные выше и делает тоже саммое только для Viewsets нужны Router 
# class PostViewsets(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# #     # переопределение queryset https://www.youtube.com/watch?v=Ur24Ms-MD5k&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=10 13:20

    
# # 8 ViewSet + action - создаём api для просмотра тегов. Action в основном пишутся только тогда когда есть какоето действие например лайкнуть пост и тд...
# class PostViewsetsTags(PostViewsets):

#     @action(methods=["get"], detail=False) # detail=True значит будет только 1 обьект
#     def tags(self, request, pk=None): # теперь по адрессу http://127.0.0.1:8000/api/post/tags/, !!! имя в url tags = имя нашей функции !!!, теперь по этому адрессу получим все теги
#         tag = Tag.objects.all()
#         print(tag)
#         return Response({'tags': [tg.name for tg in tag]})


# 9 Permission - разрешения эти разрешения пишутся permission_classes = [и сюда один из классов перечисленных снизу]
# AllowAny - полный доступ
# IsAuthenticared - только для авторизованных пользователей
# IsAdminUser - только для админов
# IsAuthenticatedOrReadOnly - Только  для авторизованных или всем но только чтения 
from rest_framework import permissions
class IsAdminOrReadOnly(permissions.BasePermission): # Cвйо класс. Если пользователь админ может удалть в противном случае может только смотерть GET
    def has_permission(self,request,view): return bool(request.user.is_staff or request.method in ["GET",])
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj): return bool(obj.user == request.user or request.method in ["GET",])
# пример на обычных классах generics 
class PostList(generics.ListAPIView): # данный класс позволяет прасматривать список всех постов их может смотреть любой пользователь AllowAny
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 
    permission_classes = [AllowAny, ]
class PostCreate(generics.CreateAPIView): # позволяет изменять по id обьект только для авторизавыннх пользователей
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
class PostUpdate(generics.UpdateAPIView): # позволит изменять пост только а втору
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    peermission_classes = [IsAuthorOrReadOnly]
class PostDelete(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer 
    permission_classes = [IsAdminOrReadOnly]


#10 авторизация на основе сесии и cookies