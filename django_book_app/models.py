from django.db import models
from datetime import date
from django.urls import reverse


class Author(models.Model):
    """Автор"""
    name = models.CharField("Имя", max_length=100)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="authors/")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    """Книга"""
    title = models.CharField("Название", max_length=100)
    tagline = models.CharField("Слоган", max_length=100, default='')
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="books/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    country = models.CharField("Страна", max_length=30)
    authors = models.ManyToManyField(Author, verbose_name="авторы", related_name="book_author")
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
