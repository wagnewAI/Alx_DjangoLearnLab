# Advanced API Project

## Book Endpoints

- **GET /api/books/** → List all books (public).
- **GET /api/books/<id>/** → Retrieve a specific book (public).
- **POST /api/books/create/** → Create a new book (authenticated only).
- **PUT /api/books/<id>/update/** → Update an existing book (authenticated only).
- **DELETE /api/books/<id>/delete/** → Delete a book (authenticated only).

### Permissions
- Public: List and Retrieve
- Authenticated: Create, Update, Delete

### Notes
- Custom validation ensures `publication_year` cannot be in the future.
- Nested relationship: Authors show their related books via `AuthorSerializer`.
## 2. Implementing Filtering, Searching, and Ordering in Django REST Framework
## Book List API with Advanced Queries

- **Filtering**
  - By title, author ID, publication_year
  - Example: `/api/books/?author=1&publication_year=1997`

- **Search**
  - Partial text search on title and author name
  - Example: `/api/books/?search=Harry`

- **Ordering**
  - Sort by title, publication_year, or author
  - Prefix `-` for descending
  - Example: `/api/books/?ordering=-publication_year`

- **Combined usage**
  `/api/books/?author=1&search=Harry&ordering=-publication_year`
## Now my BookListView supports:

  - Filtering
  - Search
  - Ordering
  - Fully testable via API tools.
  # 3.
  #Testing strategy:

# CRUD Operations

  - Create: authenticated vs unauthenticated users.
  - Update: modify book fields.
  - Delete: remove book instance.
  - Retrieve & List: confirm correct response data.
  - Advanced Queries
  - Filtering by author.
  - Searching by title.
  - Ordering by publication_year.

# Permissions
  - Ensure unauthenticated users cannot create, update, or delete books.

# How to run tests:
   - Bash: python manage.py test api
# Interpreting results:

  - OK → all tests passed.
  - FAIL / ERROR → investigate which test failed, check the response data and status code.