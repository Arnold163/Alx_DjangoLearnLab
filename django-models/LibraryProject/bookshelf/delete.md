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