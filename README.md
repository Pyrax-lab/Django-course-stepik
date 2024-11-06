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

        'django.contrib.auth.backends.ModelBackend', <--- вот этот шаблон записываем всегда так как он разрешает авторизовыватся через стандартный пароль 
    ) 
    далее в TEMPLATES -> context_processors добавляем эти 2 строки
                **'social_django.context_processors.backends',**
                **'social_django.context_processors.login_redirect',**
Использованеи: В главном файле urls добавить такой путь **re_path(r'^oauth/', include('social_django.urls', namespace='social')),**
 

--сюда нужно передать ключи которые нам выдал гит хаб. Эти ключи относится не к вашему пользователю а именно к вашему приложению так что други люди смогут так же регистрироватся через их ний гит хаб а вам уже будет приходить токен с email username и тд..--

###GitGub###
**SOCIAL_AUTH_GITHUB_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxx'** 
**SOCIAL_AUTH_GITHUB_SECRET = 'xxxxxxxxxxxxxxxx'**
**<a href="{% url 'social:begin' 'github' %}">Log In with GitHub</a>** непосредственно ссылка для регистрации по GitHub 


###Google###
**SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'xxxxxxxxxxxxxxxxxxxx'**
**SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'xxxxxxxxxxxxxxxx'**
**<br><a href="{% url 'social:begin' 'google-oauth2' %}">Log In with Google</a>**

#Как сохранить секреты в безопасности?#
Часто при работе над проектом Django у нас есть секретные ключи, ключи OAuth и другая важная информация, которую необходимо хранить в безопасности и конфиденциальности. Вы ни в коем случае не должны раскрывать такие ключи, потому что это делает вашу систему уязвимой для атак безопасности.

Как мы можем прочитать из документации, в основном, что делает python-dotenv, это считывает пары ключ-значение из файла .env и устанавливает их как переменные среды для последующего извлечения.

Папка или файл .env (сокращение от "environment") используется для хранения конфиденциальной информации, такой как ключи API, пароли и другие настройки окружения, которые не должны попадать в систему контроля версий (например, Git)


Устанавливаем модуль 

**pip install python-dotenv**


Дальше создаем файл с названием .env
Здесь указавыем Ключь = Значение(пароль)

**SECRET_KEY = 'django-insecure-xxxxxxxxx'**

**GITHUB_KEY = 'xxxxxxxxx'**
**GITHUB_SECRET = 'xxxxxxxxxxxxxxxxxx'**

**GOOGLE_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'**
**GOOGLE_SECRET = 'xxxxxxxxxxxxxxxxxx**

В settings добавляем данные код  , он позволяет из файла .env загружать переменные которые хранят в себе ключи 
from dotenv import load_dotenv
import os
load_dotenv()


чтобы получить значение какого ключа нужно написать его имя в нутри функции getenv() предварительно импортировав библиотеку os
str(os.getenv("GOOGLE_KEY")) 

