from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework 
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter # Import OrderingFilter here



# Latest Django views
# ListView:
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year'] # Enable filtering by these fields
    search_fields = ['title', 'author'] # Enable search by title and author
    ordering_fields = ['title', 'publication_year'] # Allow ordering by title and publication_year

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


# Traditional Django views
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

# ListView: Retrieve all books (no authentication required)
class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'  # Specify your template

# DetailView: Retrieve a single book by ID (no authentication required)
class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'  # Specify your template

# CreateView: Only authenticated users can create books
class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')  # Redirect after successful creation

# UpdateView: Only authenticated users can update books
class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'publication_year', 'author']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book-list')  # Redirect after successful update

    # Ensure the user trying to update the book is allowed (customize this logic as needed)
    def test_func(self):
        # Customize this logic as per your needs (e.g., owner of the book)
        return self.request.user.is_authenticated

# DeleteView: Only authenticated users can delete books
class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

    # Ensure the user trying to delete the book is allowed (customize this logic as needed)
    def test_func(self):
        # Customize this logic as per your needs (e.g., owner of the book)
        return self.request.user.is_authenticated