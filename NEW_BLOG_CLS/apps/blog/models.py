from django.db import models

# Create your models here.


from django.db import models
from django.core.validators import FileExtensionValidator 
from django.contrib.auth import get_user_model 


class Post(models.Model):
    """
    Модель пост
    """

    title = models.CharField(verbose_name = "Название поста", max_length = 255)
    slug = models.SlugField(verbose_name = "URL", blank=True, uniqu=True)
    text = models.TextField(verbose_name = "Описание")
    photo_post = models.ImageField(verbose_name = "Фото для поста", blank=True, default = "default.png", upload_to = "image/photos_blogs",validators=[FileExtensionValidator(allowed_extension=('png', 'gif', 'jpg', 'jpeg'))])
    created = models.DateTimeField(auto_now_add = True, verbose_name = 'Время добавления')
    update = models.DateTimeField(auto_now = True, verbose_name = "Дата обновления")
    author = models.ForeignKey(to=get_user_model(), default = 1, related_name = 'author_posts', on_delete = models.SET_DEFAULT, verbose_name = 'Автор')
    updater = models.ForeignKey(to=get_user_model(), default = 1, null = True, on_delete = models.SET_NULL, verbose_name = 'Обновил', related_name = "updater_posts")
    fixed = models.BooleanField(verbose_name = "Прикрепленно", default = False)
    class Meta:
        db_table = "blog_post"
        ordering = ['fixed', '-created']
        verbose_name = 'Статья'
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title
