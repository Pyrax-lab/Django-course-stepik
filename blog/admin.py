from django.contrib import admin
from .models import Post, Coment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug" : ("title",)}
    search_fields = ["title", "body"]
    autocomplete_fields = ['auth']
    ordering = ["publish"]
    date_hierarchy = "publish"


@admin.register(Coment)
class ComentAdmin(admin.ModelAdmin):
    ordering = ["created"]