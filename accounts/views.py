from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView  # Импортируем стандартное представление LoginView из django.contrib.auth.views
from .forms import SignUp, LoginForm

from django.views import generic 
from django.urls import reverse_lazy
# Create your views here.


class CustomLoginView(LoginView): # Создаем кастомный класс для входа, наследуемый от LoginView
    form_class = LoginForm # Задаем форму для входа (должен быть созданный класс формы LoginForm)

    def form_valid(self, form): # Метод вызывается, когда форма логина валидна
        remember_me = form.cleaned_data.get("remember_me") # Получаем значение чекбокса 'remember_me' из очищенных данных формы

        if not remember_me: # Если 'remember_me' не выбрано (None или False)
            self.request.session.set_expiry(0) # Устанавливаем срок действия сессии на 0, что означает завершение сессии при закрытии браузера
            self.request.session.modified = True  # Указываем, что сессия была изменена, чтобы сохранить изменения


        return super(CustomLoginView, self).form_valid(form) # Вызываем метод form_valid родительского класса, который завершает процесс логина


class SignUpView(generic.CreateView): # Регистрация
    form_class = SignUp
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"