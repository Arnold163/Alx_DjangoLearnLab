from django.shortcuts import render
from django.views.generic import DetailView
from models import Book, Library

# Create your views here.

# function based view
def list_books(request):
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

# class based view
class library_detail(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

    


