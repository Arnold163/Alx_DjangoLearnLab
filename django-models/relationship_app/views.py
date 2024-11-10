# relationship_app/views.py

from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Corrected import

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Updated template path

# Class-based view to display library details
class LibraryDetailView(DetailView):  # Renamed to follow CamelCase convention
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Updated template path
    context_object_name = 'library'




