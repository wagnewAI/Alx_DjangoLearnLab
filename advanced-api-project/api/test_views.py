from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book


class BookAPITestCase(TestCase):
    """
    Test suite for the Book API endpoints.
    Covers CRUD operations, filtering, searching, ordering, and permission checks.
    """

    def setUp(self):
        """
        Set up test data and API client.
        """
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()

        # Create authors
        self.author1 = Author.objects.create(name="J.K. Rowling")
        self.author2 = Author.objects.create(name="Tolkien")

        # Create books
        self.book1 = Book.objects.create(title="Harry Potter", publication_year=1997, author=self.author1)
        self.book2 = Book.objects.create(title="The Hobbit", publication_year=1937, author=self.author2)

    # -----------------------------
    # TESTING LIST AND RETRIEVE
    # -----------------------------
    def test_list_books(self):
        """Test retrieving list of books"""
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        """Test retrieving a single book"""
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Harry Potter")

    # -----------------------------
    # TESTING CREATE
    # -----------------------------
    def test_create_book_unauthenticated(self):
        """Unauthenticated users cannot create a book"""
        self.client.force_authenticate(user=None)  # explicitly unauthenticated
        response = self.client.post("/api/books/create/", {
            "title": "New Book",
            "publication_year": 2025,
            "author": self.author1.id
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_book_authenticated(self):
        """Authenticated users can create a book"""
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/books/create/", {
            "title": "Fantastic Beasts",
            "publication_year": 2001,
            "author": self.author1.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], "Fantastic Beasts")

    # -----------------------------
    # TESTING UPDATE
    # -----------------------------
    def test_update_book(self):
        """Test updating a book"""
        self.client.force_authenticate(user=self.user)
        response = self.client.put(f"/api/books/{self.book1.id}/update/", {
            "title": "Harry Potter Updated",
            "publication_year": 1998,
            "author": self.author1.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Harry Potter Updated")

    # -----------------------------
    # TESTING DELETE
    # -----------------------------
    def test_delete_book(self):
        """Test deleting a book"""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/books/{self.book1.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -----------------------------
    # TESTING FILTER, SEARCH, ORDER
    # -----------------------------
    def test_filter_books_by_author(self):
        """Test filtering books by author"""
        response = self.client.get(f"/api/books/?author={self.author2.id}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "The Hobbit")

    def test_search_books_by_title(self):
        """Test searching books by title"""
        response = self.client.get("/api/books/?search=Harry")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_order_books_by_publication_year_desc(self):
        """Test ordering books by publication year descending"""
        response = self.client.get("/api/books/?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 1997)
        self.assertEqual(response.data[1]['publication_year'], 1937)
