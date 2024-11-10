from relationship_app.models import Author, Book

author = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author)
for book in books_by_author:
    print(book.title)