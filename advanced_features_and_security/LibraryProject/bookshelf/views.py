from django.shortcuts import render

# Create your views here.
from .models import Book
from .forms import BookSearchForm

def book_search(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        query = form.cleaned_data['query']
        # Safe ORM query; avoids SQL injection
        books = Book.objects.filter(title__icontains=query)
    return render(request, "bookshelf/book_list.html", {"books": books, "form": form})
