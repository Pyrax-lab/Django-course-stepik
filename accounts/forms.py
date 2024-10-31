from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

from .models import Profile

class SignUp(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=150)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=150, required=True, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    password = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput(attrs={"placeholder":"Пароль"}))
    remember_me = forms.BooleanField(required=False)


    class Meta:
        model  = User
        fields = ["username", "password", "remember_me"]




class UpdateUserForm(forms.ModelForm): # Взаимодействует с моделю пользоватлея позваляя изменять имя и email пользователя

    username = forms.CharField(max_length = 150, required=True, widget = forms.TextInput())
    email    = forms.EmailField(max_length=150, required=True, widget = forms.TextInput())

    class Meta:
        model = User 
        fields = ["username", "email"]


class UpdateProfileForm(forms.ModelForm): # Взаимодействует с профилям пользвателя позволяя изменять картинку(профиля) и биографию

    image = forms.ImageField(widget=forms.FileInput())
    bio = forms.CharField(widget=forms.TextInput(attrs={'rows':5}))

    class Meta:
        model = Profile 
        fields = ["image", "bio"]
