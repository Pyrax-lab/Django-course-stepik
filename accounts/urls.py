from django.urls import path
from .views import SignUpView, CustomLoginView

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = "signup"),
    path("login/", CustomLoginView.as_view(redirect_authenticated_user = True, template_name = "registration/login.html"), name= "login")
]

# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']

# идет автоматически если мы подключи path("accounts/", include("django.contrib.auth.urls"))