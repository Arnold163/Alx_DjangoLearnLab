# Retrieve Operation
# Command 
```python 
>>> from bookshelf.models import Book
# retrieve the book
>>> book = Book.objects.get(title="1984")                          
>>> book.title, book.author, book.publication_year

# expected output
('1984', 'George Orwell', 1949)