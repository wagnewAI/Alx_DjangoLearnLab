from relationship_app.models import Author, Book, Library, Librarian
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
         return []

# Query 2: List all books in a specific library
def get_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return []

# Query 3: Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian.name
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None

# Example usage
if __name__ == "__main__":
    print(get_books_by_author("George Orwell"))        # [<Book: 1984>, <Book: Animal Farm>]
    print(get_books_in_library("City Library"))       # [<Book: 1984>, <Book: Animal Farm>]
    print(get_librarian_for_library("City Library"))  # Alice