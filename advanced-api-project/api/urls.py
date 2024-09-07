from django.contrib import admin
from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin site
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # View a single book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a new book  
    path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),  # Update an existing book
    path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]
