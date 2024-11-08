#CRUD_operations
# Create Operation

## Command:
```python
from bookshelf.models import Book

# Create a new Book instance
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

#expected output 
<Book: 1984 by George Orwell (1949)>


# Retrieve Operation
# Command 
```python 
>>> from bookshelf.models import Book
# retrieve the book
>>> book = Book.objects.get(title="1984")                          
>>> book.title, book.author, book.publication_year

# expected output
('1984', 'George Orwell', 1949)

# Update Operation
# Commands 
```python

from bookshelf.models import Book

#update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
# confirm update
book

#expected output
<Book: Nineteen Eighty-Four by George Orwell (1949)>


# Delete Operation
# Commands

```python
>>> from bookshelf.models import Book   

# delete the instance 
>>> book.delete()
(1, {'bookshelf.Book': 1})

#confirm delete
>>> Book.objects.all()

#expected output
<QuerySet []>
>>>