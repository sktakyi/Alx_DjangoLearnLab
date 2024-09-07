from django.contrib import admin
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from django.urls import path, include

urlpatterns = [
     path('admin/', admin.site.urls),  # Django Admin
    path('api/', include('api.urls')),  # Include the api app's URLs under the 'api/' path
    path('books/', BookListView.as_view(), name='book-list'),  # List all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # View a single book by ID
    path('books/create/', BookCreateView.as_view(), name='book-create'),  # Create a new book
    path('books/update/', BookUpdateView.as_view(), name='book-update'),  # Update an existing book
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete a book
]