from django.urls import path , include
from .views import PostList,PostUpdate, PostGetUpdateDelete, PostViewsets #, PostDetail


from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"post", PostViewsets, basename="post")

urlpatterns = [
    # path("<int: pk>/", PostDetail.as_views(), name="post_detail"),
    # path("", PostList.as_view(), name="post_list"),
    # path("/<int:pk>/",PostUpdate.as_view(), name="post_list_post"), # изменяем конкретный обьект
    # path("/postdetail/<int:pk>/", PostGetUpdateDelete.as_view(), name="post_detail_pk")# получить изменить и удлать конкретный обьект

    #ViewSets

    # path("", PostViewsets.as_view({"get": 'list'}), name="post_list"),
    # path("/<int:pk>/", PostViewsets.as_view({"post": "retrieve", "delete": "destroy"}),name="post_list_post")

    #Router

    path("/", include(router.urls)) # если мы используем обьект роутера то он автоматически создаст create, get, delit put  методы и так же сможет принимать id обьекта
    
]
