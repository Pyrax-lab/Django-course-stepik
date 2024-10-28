

from django.urls import path
from . import views


app_name = "blog"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("tags/<slug:tag_slug>", views.post_list, name="post_list_by_tag"),

    path("<int:year>/<int:month>/<int:day>/<slug:post>/", views.post_detail, name="post_detail"),
    #path("coment/<int:post_id>", views.post_detail,name = "post_coment"),


    path("share/<int:post_id>", views.post_share, name = "post_share"),
    
]