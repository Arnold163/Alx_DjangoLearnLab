# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.views import View
from .models import Book, Library

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# RegisterView for user registration
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

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

# Custom logout view
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
    template_name = 'relationship_app/login.html'

    # logout view
    class CustomLogoutView(LogoutView):
        template_name = 'relationship_app/logout.html'


