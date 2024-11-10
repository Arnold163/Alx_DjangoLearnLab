from relationship_app.models import Author, Book
# all books by a specific author
author = Author.objects.get(name="author_name")
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)

from relationship_app.models import Library
# list all books in library
library = Library.objects.get(name="library_name")
books_in_library = library.books.all()
for book in books_in_library:
    print(book.title)

from relationship_app.models import Library, Librarian
# Retrive the librarian for a library
library = Library.objects.get(name="library_name")
librarian = Librarian.objects.get(library=library)
print(librarian.name)