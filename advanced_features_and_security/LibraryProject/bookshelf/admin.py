from django.contrib import admin

# Register your models here.
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

#admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    #fields to be displayed in the list view
    list_display = ('title', 'author', 'publication_year')

    #filter options 
    list_filter = ('author', 'publication_year')

    #search functionality 
    search_fields = ('title', 'author_name',)

    #Register book modele with custom admin
admin.site.register(Book, BookAdmin)

class CustomUserAdmin(UserAdmin):
    # Define the additional fields you want displayed in the admin
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

# Register the CustomUser model with the CustomUserAdmin configuration
admin.site.register(CustomUser, CustomUserAdmin)