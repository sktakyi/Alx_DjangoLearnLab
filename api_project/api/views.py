from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.viewsets import ModelViewSet  # Import ModelViewSet directly
from .models import Book
from .serializers import BookSerializer

# BookList for listing books
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# BookViewSet for full CRUD operations
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
