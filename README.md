На данный момент прожу платный курс на степике по Django https://stepik.org/course/174634/promo и на основе это курса создаю проект. В рамках этого курса создаётся блог 


Что узнал нового из этого курса 
1) < -Xutf8 manage.py dumpdata --indent=2 --output=mysite_data.json > 
Данная строка позволяет все таблица из бд закинуть в один файл что бывает очень полезно иметь все в одном файле


2) Использовалась библиотека django-taggit позволяющия создавать очень легко тегги 
Устнаовка:   pip install djang-taggit
Подключение: в settings -> INSTALLED_APPS -> "taggit" ,  В models подключаем её from taggit.managers import TaggableManager
Использованеи: В нашей модели используем её tags = TaggableManager()