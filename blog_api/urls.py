from django.urls import path , include
#from .views import PostViewsets, PostViewsetsTags #, PostDetail


# from rest_framework import routers
# # 1. Используем SimpleRouter
# router = routers.SimpleRouter()
# router.register(r"post", PostViewsetsTags, basename="post")
# # Теперь по адресу http://127.0.0.1:8080/api/post/ 
# # мы сможем получить список всех постов.
# # SimpleRouter создаёт маршруты только для ресурсов, которые мы зарегистрировали.



# # 2. Используем DefaultRouter
# router = routers.DefaultRouter()
# router.register(r"post", PostViewsetsTags, basename="post")
# # Помимо маршрутов для ресурсов, таких как http://127.0.0.1:8080/api/post/, 
# # DefaultRouter также добавляет страницу со схемой API 
# # по адресу http://127.0.0.1:8080/api/.
# # На этой странице отображается описание всех зарегистрированных маршрутов.


# urlpatterns = [
#     # path("<int: pk>/", PostDetail.as_views(), name="post_detail"),
#     # path("", PostList.as_view(), name="post_list"),
#     # path("/<int:pk>/",PostUpdate.as_view(), name="post_list_post"), # изменяем конкретный обьект
#     # path("/postdetail/<int:pk>/", PostGetUpdateDelete.as_view(), name="post_detail_pk")# получить изменить и удлать конкретный обьект

#     #ViewSets

#     # path("", PostViewsets.as_view({"get": 'list'}), name="post_list"),
#     # path("/<int:pk>/", PostViewsets.as_view({"post": "retrieve", "delete": "destroy"}),name="post_list_post")

#     #Router

#     path("/", include(router.urls)) # если мы используем обьект роутера то он автоматически создаст create, get, delit put  методы и так же сможет принимать id обьекта
    
# ]

from .views import PostList,PostCreate, PostDelete

urlpatterns = [
    path("/post/", PostList.as_view(), name="post_list"),
    path("/post/create/", PostCreate.as_view(), name="post_create"),
    path("/post/<int:pk>/", PostDelete.as_view(), name="post_delete"),
    #path("post/<int:pk>")
]