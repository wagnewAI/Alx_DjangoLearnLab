from django.contrib import admin

# Register your models here.
from .models import Book

# Custom admin class
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in the admin list view
    search_fields = ('title', 'author')                     # Add search by title or author
    list_filter = ('publication_year',)                     # Filter by publication year

# Register the model with the custom admin
admin.site.register(Book, BookAdmin)