from django.urls import path
from . import views
from .views import list_books
from .views import CustomLoginView, CustomLogoutView, RegisterView
from .views import list_books, RegisterView, CustomLoginView, CustomLogoutView
from .views import admin_view, librarian_view, member_view


urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # URL for user registration (class-based view)
    path('register/', RegisterView.as_view(), name='register'),

    # URL for login (custom class-based view)
    path('login/', CustomLoginView.as_view(), name='login'),

    # URL for logout (custom class-based view)
    path('logout/', CustomLogoutView.as_view(), name='logout'), 
    
    path('register/', views.register),

    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html')),
    path ('login/', LoginView.as_view(template_name='relationship_app/login.html')),

    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    
]