from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.list_books, name="list_books"),  # FBV
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # CBV
    # Authentication URLs
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
      # Role-based URLs
    path("admin-view/", views.admin_view, name="admin_view"),
    path("librarian-view/", views.librarian_view, name="librarian_view"),
    path("member-view/", views.member_view, name="member_view"),
    # Secured book operations
    path("book/add/", views.add_book, name="add_book"),
    path("book/edit/<int:pk>/", views.edit_book, name="edit_book"),
    path("book/delete/<int:pk>/", views.delete_book, name="delete_book"),
]
