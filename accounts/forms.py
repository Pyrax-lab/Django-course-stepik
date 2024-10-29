from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms

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