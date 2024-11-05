На данный момент прожу платный курс на степике по Django https://stepik.org/course/174634/promo и на основе это курса создаю проект. В рамках этого курса создаётся блог 


Что узнал нового из этого курса 
1) < -Xutf8 manage.py dumpdata --indent=2 --output=mysite_data.json > 
Данная строка позволяет все таблица из бд закинуть в один файл что бывает очень полезно иметь все в одном файле


2) Использовалась библиотека django-taggit позволяющия создавать очень легко тегги 
Устнаовка:   pip install djang-taggit
Подключение: в settings -> INSTALLED_APPS -> "taggit" ,  В models подключаем её from taggit.managers import TaggableManager
Использованеи: В нашей модели используем её **tags = TaggableManager()**



3) Использование библиотеки social-auth-app-django позволяющаяя регестрироватся через социальные сети
Установка: pip install social-auth-app-django
Подключение: в settings -> INSTALLED_APPS -> 'social_django' применяем миграции далее создаём новую перменную **AUTHENTICATION_BACKENDS = (**
        **'social_core.backends.github.GithubOAuth2',**
        **'social_core.backends.google.GoogleOAuth2',**

        **'django.contrib.auth.backends.ModelBackend',** <--- вот этот шаблон записываем всегда так как он разрешает авторизовыватся через стандартный пароль 
    ) 
    далее в TEMPLATES -> context_processors добавляем эти 2 строки
                **'social_django.context_processors.backends',**
                **'social_django.context_processors.login_redirect',**
Использованеи: В главном файле urls добавить такой путь **re_path(r'^oauth/', include('social_django.urls', namespace='social')),**
 
 SOCIAL_AUTH_GITHUB_KEY = 'YOUR GITHUB KEY'
SOCIAL_AUTH_GITHUB_SECRET = 'YOUR GITHUB SECRET KEY'

<a href="{% url 'social:begin' 'github' %}">Log In with GitHub</a>
