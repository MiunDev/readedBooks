from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from django_book_app.models import Book


class BookView(ListView):
    """Список книг"""

    model = Book
    # получаем список книг, исключая книги в черновиках через поле draft
    queryset = Book.objects.filter(draft=False)
    template_name = "books/book_list.html"


class BookDetailView(View):
    """Полное описание фильма"""

    # model = Book
    # slug_field = "url"

    def get(self, request, slug):
        book = Book.objects.get(url=slug)
        return render(request, "books/book_detail.html", {"book": book})
