# relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library  
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book
from .forms import BookForm

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})  

# Class-based view to display library details
class LibraryDetailView(DetailView):  
    model = Library
    template_name = 'relationship_app/library_detail.html'  
    context_object_name = 'library'

# class registration view
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'relationship_app/register.html', {'form': form})
    
    # login view
    class CustomLoginView(LoginView):
        template_name = 'relationship_app/login.html'

    # logout view
    class CustomLogoutView(LogoutView):
        template_name = 'relationship_app/logout.html'

    # Role based views helper functions
    def is_admin():
        return hasattr(user, 'userprofile') and user.userprofile.role == 'admin'
    
    def is_library(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == 'library'
    
    def is_member(user):
        return hasattr(user, 'userprofile') and user.userprofile.role == 'member'
    
   # Admin view, accessible only to users with the 'admin' role
    @user_passes_test(admin_test)
    def admin_view(request):
     return render(request, 'relationship_app/admin_view.html')

# Library view, accessible only to users with the 'library' role
    @user_passes_test(is_library, login_url='/access-denied/')
    def library_view(request):
        return render(request, 'relationship_app/library_view.html')

# Member view, accessible only to users with the 'member' role
    @user_passes_test(is_member, login_url='/access-denied/')
    def member_view(request):
        return render(request, 'relationship_app/member_view.html')
    
    def access_denied(request):
        return render(request, 'relationship_app/access_denied.html')


    @permission_required('relationship_app.can_add_book', raise_exception=True)
    def add_book(request):
        if request.method == 'POST':
            form = BookForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('book_list')  # redirect to a list of books or another appropriate page
        else:
            form = BookForm()
        return render(request, 'relationship_app/add_book.html', {'form': form})

    @permission_required('relationship_app.can_change_book', raise_exception=True)
    def edit_book(request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if request.method == 'POST':
            form = BookForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                return redirect('book_list')
        else:
            form = BookForm(instance=book)
        return render(request, 'relationship_app/edit_book.html', {'form': form})

    @permission_required('relationship_app.can_delete_book', raise_exception=True)
    def delete_book(request, book_id):
        book = get_object_or_404(Book, id=book_id)
        if request.method == 'POST':
            book.delete()
            return redirect('book_list')
        return render(request, 'relationship_app/delete_book.html', {'book': book})
