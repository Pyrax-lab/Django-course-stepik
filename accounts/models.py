from django.db import models
from django.contrib.auth.models import User, AbstractUser



# Create your models here.



class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="default.jpg", upload_to='images', verbose_name = "Картинка пользователя")
    bio = models.TextField(verbose_name="Биография")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"