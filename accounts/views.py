from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import LoginView  # Импортируем стандартное представление LoginView из django.contrib.auth.views
from .forms import SignUp, LoginForm, UpdateProfileForm, UpdateUserForm

from django.views import generic 
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
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
    initial = None # {key: value}


    # если get запрос
    def get(self, request, *args , **kwargs):
        form = self.form(initial = self.initial) # в initial можно передать значения по умолчанию 
        return(render, request, self.template_name, {"form" : form})

    # если post запрос
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            return redirect(to="/")
        

        return render(request, self.template_name, {"form": form})



    


    def dispatch(self, request, *args, **kwargs) -> HttpResponse:
        if request.user.is_authenticated:
            return redirect(to='/')
        
        return super(SignUpView, self).dispatch(request, *args, **kwargs)
    

# class SignUpView(generic.CreateView): , Представление для регистрации, наследуемое от generic.CreateView для упрощенной работы с формами создания.
#     form_class = SignUpForm , Указывает форму, которая будет использоваться для создания нового пользователя.    
#     success_url = reverse_lazy("login") , Указывает URL для перенаправления после успешной регистрации. Здесь используется отложенное вычисление URL с помощью `reverse_lazy`.    
#     initial = None , Начальные данные для формы, принимает словарь значений {'key': 'value'}.    
#     template_name = 'registration/signup.html' ,  Шаблон, который будет использоваться для отображения страницы регистрации.

#     def dispatch(self, request, *args, **kwargs):,   Метод `dispatch` обрабатывает запрос и направляет его к нужному методу (get, post и т.д.).
#         if request.user.is_authenticated: , Проверяет, аутентифицирован ли пользователь.
#             return redirect(to='/') , Если пользователь аутентифицирован, перенаправляет его на главную страницу, чтобы избежать повторной регистрации.
#         return super(SignUpView, self).dispatch(request, *args, **kwargs) , Если пользователь не авторизован, вызывает метод `dispatch` родительского класса, который обрабатывает запрос дальше.

#     def get(self, request, *args, **kwargs):,  Метод для обработки GET-запроса, вызывается при посещении страницы регистрации.
#         form = self.form_class(initial=self.initial), Создает экземпляр формы с указанными начальными данными.
#         return render(request, self.template_name, {'form': form}), Отображает шаблон регистрации с формой на странице.

#     def post(self, request, *args, **kwargs):, метод для обработки POST-запроса, вызывается при отправке данных формы.
#         form = self.form_class(request.POST) ,Создает экземпляр формы с данными, полученными от пользователя.
#         if form.is_valid():, Проверяет, валидна ли форма (корректные и обязательные данные).
#             form.save() , Сохраняет данные формы, создавая нового пользователя.
#             username = form.cleaned_data.get('username') , Извлекает введенное имя пользователя из очищенных данных формы.
#             messages.success(request, f'Account created for {username}') , Создает сообщение об успешной регистрации для пользователя.
#             return redirect(to='login') , Перенаправляет пользователя на страницу логина после успешной регистрации.
#         return render(request, self.template_name, {'form': form}) ,Если форма не прошла проверку, снова отображает страницу регистрации с формой и ошибками.




@login_required
def profile(request):


    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
    

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(to="user-profile")
        
    else:
        user_form = UpdateProfileForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)


    return render(request, "registration/profile.html", context={"user_form": user_form, "profile_form": profile_form})