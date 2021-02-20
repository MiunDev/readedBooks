from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from django_book_app.forms import ReviewForm
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


class AddReview(View):
    """Отзывы"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        book = Book.objects.get(id=pk)  # запрос в БД для получения объекта с фильмом
        if form.is_valid():
            form = form.save(commit=False)  # приостановка сохранения формы для внесения каких то изменений
            if request.POST.get("parent", None):  # если поле parent (на странице) не пустое
                form.parent_id = int(request.POST.get("parent"))  # то заполняем поле parent у отзыва
            form.book = book  # передаем объект Movie из БД для формы
            form.save()  # сохранение данных формы в БД
        return redirect(book.get_absolute_url())
