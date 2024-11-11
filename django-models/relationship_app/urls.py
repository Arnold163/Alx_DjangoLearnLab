from django.urls import path
from . import views
from .views import list_books
from .views import CustomLoginView, CustomLogoutView, RegisterView
from .views import list_books, RegisterView, CustomLoginView, CustomLogoutView
from .views import admin_view, library_view, member_view, access_denied


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
    path('library/', library_view, name='library_view'),
    path('member/', member_view, name='member_view'),
    path('access-denied/', access_denied, name='access_denied'),


     path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    
]