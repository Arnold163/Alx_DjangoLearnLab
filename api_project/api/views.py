from rest_framework.generics import generics.ListAPIView
from rest_framework.viewsets import BookViewSet
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets.ModelViewSet

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(BookViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
