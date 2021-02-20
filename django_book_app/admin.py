from django.contrib import admin
from .models import Book, Author, Reviews


# конфигурирование наших записей в админке
class ReviewInline(admin.TabularInline):
    model = Reviews
    readonly_fields = ("name", "email")


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "parent", "book", "id")
    readonly_fields = ("name", "email")
    inlines = [ReviewInline]


admin.site.register(Book)
admin.site.register(Author)
