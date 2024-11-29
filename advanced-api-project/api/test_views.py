from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from api.models import Book

class BookAPITestCase(APITestCase):
    
    def setUp(self):
        #create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        #sample book creation 
        self.book1 = Book.objects.create(title='Book 1', author='Author 1', description='Description 1')
        self.book2 = Book.objects.create(title='Book 2', author='Author 2', description='Description 2')

        #endpoint Url
        self.url = '/api/books/'
    
    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'description': 'New Description'
        }

        response = self.client.post(self.url, data)
        self.assertAlmostEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_get_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book(self):
        data = {
            'title': 'Updated Book 1',
            'author': 'Updated Author 1',
            'description': 'Updated Description 1'
        }
        response = self.client.put(f'{self.url}{self.book1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book 1')

    def test_delete_book(self):
        response = self.client.delete(f'{self.url}{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        response = self.client.get(self.url, {'author': 'Author 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author 1')

    def test_search_books(self):
        response = self.client.get(f'{self.url}?search=Book 1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book 1')

    def test_order_books(self):
        response = self.client.get(f'{self.url}?ordering=title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Book 1')
        self.assertEqual(response.data[1]['title'], 'Book 2')

    def test_permissions(self):
        self.client.logout()
        response = self.client.post(self.url, {'title': 'Unauthorized Book'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        

        