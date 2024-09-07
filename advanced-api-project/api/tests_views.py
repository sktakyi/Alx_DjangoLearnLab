from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book
from django.contrib.auth.models import User

class BookAPITests(TestCase):
    def setUp(self):
        # Set up the API client and test data
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        
        self.book = Book.objects.create(title='Test Book', author='Test Author', publication_year=2023)
        self.create_url = reverse('book-list')
        self.update_url = reverse('book-update', args=[self.book.pk])
        self.delete_url = reverse('book-delete', args=[self.book.pk])
        self.detail_url = reverse('book-detail', args=[self.book.pk])
    
    def test_create_book(self):
        response = self.client.post(self.create_url, {'title': 'New Book', 'author': 'New Author', 'publication_year': 2024}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
    
    def test_read_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')
    
    def test_update_book(self):
        response = self.client.put(self.update_url, {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2025}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')
    
    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        response = self.client.get(self.create_url, {'title': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_search_books(self):
        response = self.client.get(self.create_url, {'search': 'Test Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_order_books(self):
        response = self.client.get(self.create_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['results'][0]['publication_year'] <= response.data['results'][1]['publication_year'])
