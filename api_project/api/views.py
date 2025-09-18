
# Secured BookViewSet with IsAuthenticated (or other permissions).
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, permissions 
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
# New CRUD ViewSet
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  
 
