from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# ListView: Retrieve all books
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Allow unauthenticated users to read

# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Authenticated users can update/delete


# ListView: Retrieve all books (GET) and Create a new book (POST)
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Unauthenticated users can read, authenticated users can create

# DetailView: Retrieve a single book (GET), Update a book (PUT/PATCH), and Delete a book (DELETE)
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only authenticated users can update/delete


# ListView: Retrieve all books (GET)
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'  # Specify your template path

# DetailView: Retrieve a single book by ID (GET)
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'  # Specify your template path

# CreateView: Add a new book (POST)
class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'books/book_form.html'  # Specify your template path
    success_url = reverse_lazy('book-list')  # Redirect to the book list after a successful creation

# UpdateView: Modify an existing book (POST/PUT)
class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'books/book_form.html'  # Specify your template path
    success_url = reverse_lazy('book-list')  # Redirect to the book list after a successful update

# DeleteView: Remove a book (POST/DELETE)
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'  # Specify your template path
    success_url = reverse_lazy('book-list')  # Redirect to the book list after a successful deletion
