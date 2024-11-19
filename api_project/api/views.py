from rest_framework.generics import generics.ListAPIView
from rest_framework.viewsets import BookViewSets
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(BookViewSets):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
