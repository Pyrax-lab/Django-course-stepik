from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse
from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length = 250)
    
    body = models.TextField()

    #auth = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    auth = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name="blog_posts")

    publish = models.DateTimeField(default = timezone.now)
    slug = models.SlugField(max_length = 255, unique_for_date = "publish")

    created = models.DateTimeField(auto_now_add=True)
    update  = models.DateTimeField(auto_now = True)
    status  = models.BooleanField(blank = True, default = False)

    tags = TaggableManager() # Чтобы узнать все Тегги которые существуют надо импортирова класс Tag from taggit.models import Tag, Tag.objects.all() = все созданные тегги

    class Meta:
        ordering = ["-publish"]
        #indexes = models.Index(fields=['-publish'])
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse("blog:post_detail", 
                       args = [self.publish.year,
                               self.publish.month,
                               self.publish.day,
                               self.slug])
    

class Coment(models.Model):
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name = "coments")
    user = models.ForeignKey(get_user_model(), on_delete = models.CASCADE, related_name = "user")

    name = models.CharField(max_length = 50)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    active = models.BooleanField(default = True, blank = True, null = True)

    class Meta:
        ordering = ["created"]
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"

    def __str__(self):
        return self.name



