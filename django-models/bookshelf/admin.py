from django.contrib import admin

# Register your models here.
from .models import Book

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
