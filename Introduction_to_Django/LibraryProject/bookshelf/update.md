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
