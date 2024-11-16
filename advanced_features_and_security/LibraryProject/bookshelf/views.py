from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import ExampleForm

# Book List View
@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    # Get all books and pass them to the template
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Create Book View
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic to create a book (form handling, etc.)
    if request.method == 'POST':
        # Form submission handling
        pass
    return render(request, 'bookshelf/create_book.html')

# Edit Book View
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        # Form submission handling
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# Delete Book View
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the book list after deletion
    return render(request, 'bookshelf/delete_book.html', {'book': book})


# Example of a secure search functionality using Django ORM
def search_books(request):
    query = request.GET.get('query', '')  # Safe to use in ORM
    if query:
        books = Book.objects.filter(title__icontains=query)  # Use ORM to filter books safely
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})