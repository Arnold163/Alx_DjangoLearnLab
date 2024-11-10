# relationship_app/views.py

from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Library  
from .models import Library
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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


