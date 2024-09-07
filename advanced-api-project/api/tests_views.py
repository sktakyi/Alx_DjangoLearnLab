from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a sample Author
        self.author = Author.objects.create(name="Author 1")

        # Create some Book instances
        self.book1 = Book.objects.create(title="Book One", publication_year=2020, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2021, author=self.author)

        # URL endpoints
        self.book_list_url = reverse('book-list')
        self.book_detail_url = reverse('book-detail', kwargs={'pk': self.book1.pk})

    # Test ListView (GET all books)
    def test_get_all_books(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ensure both books are returned

    # Test DetailView (GET a single book)
    def test_get_single_book(self):
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # Test CreateView (POST a new book)
    def test_create_book(self):
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author.id  # Reference existing author
        }
        response = self.client.post(self.book_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # 3 books now in the database

    # Test UpdateView (PUT an existing book)
    def test_update_book(self):
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.put(self.book_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book Title')

    # Test DeleteView (DELETE a book)
    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Only 1 book should remain

    # Test Search Functionality
    def test_search_books(self):
        response = self.client.get(f"{self.book_list_url}?search=Book One")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    # Test Ordering Functionality
    def test_order_books(self):
        response = self.client.get(f"{self.book_list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book One')  # Oldest book first

    # Test Filtering Functionality
    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.book_list_url}?author={self.author.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # All books by the author should be returned
