from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Author model:
    - Represents an author who can write multiple books.
    - Fields:
        - name: Stores the author's full name.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model:
    - Represents a book written by an Author.
    - Fields:
        - title: Title of the book.
        - publication_year: Year the book was published.
        - author: Foreign key relationship to Author (One author can have many books).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
