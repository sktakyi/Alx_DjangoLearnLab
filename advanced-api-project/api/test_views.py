from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User


class BookAPITest(APITestCase):
    def setUp(self):
        # Set up initial data for testing.
        self.author = Author.objects.create(name="Author Name")
        self.book = Book.objects.create(
            title="Book Title",
            publication_year=2023,
            author=self.author
        )
        self.list_url = '/books/'
        self.detail_url = f'/books/{self.book.id}/'
        self.user = self.create_user()  # Create a user for authentication

    def create_user(self):
        # Helper method to create a test user.
        return User.objects.create_user(username='testuser', password='testpassword')

    def test_get_books(self):
        # Test that the list view returns a successful response.
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('results', response.data)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_book(self):
        # Test that an authenticated user can create a new book.
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'New Book',
            'publication_year': 2022,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'New Book')

    def test_update_book(self):
        # Test that an authenticated user can update an existing book.
        self.client.login(username='testuser', password='testpassword')
        data = {'title': 'Updated Title'}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Title')

    def test_delete_book(self):
        # Test that an authenticated user can delete an existing book.
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_permissions(self):
        #Test that unauthenticated users cannot create, update, or delete books.
        # Test create
        data = {'title': 'Another Book', 'publication_year': 2024, 'author': self.author.id}
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test update
        data = {'title': 'Unauthorized Update'}
        response = self.client.patch(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # Test delete
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)