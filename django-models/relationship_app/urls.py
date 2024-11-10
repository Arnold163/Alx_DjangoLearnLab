from django.urls import path
from . import views
from .views import list_books
from .views import CustomLoginView, CustomLogoutView, RegisterView
from .views import list_books, RegisterView, CustomLoginView, CustomLogoutView

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # URL for user registration (class-based view)
    path('register/', RegisterView.as_view(), name='register'),

    # URL for login (custom class-based view)
    path('login/', CustomLoginView.as_view(), name='login'),

    # URL for logout (custom class-based view)
    path('logout/', CustomLogoutView.as_view(), name='logout'), 
]