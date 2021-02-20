from django.contrib import admin
from .models import Book, Author


# конфигурирование наших записей в админке
admin.site.register(Book)
admin.site.register(Author)