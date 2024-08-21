from django.contrib import admin
from .models import Author, Book, Library, Librarian

# Register your models here.
admin.site.register((Author, Book, Library, Librarian))