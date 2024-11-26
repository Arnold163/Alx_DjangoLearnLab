from django.db import models

# Create your models here.
class Author(models.Model):
    # model representing an author
    name = models.CharField(max_length=100) #name of author

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=200) # booktitle
    publication_year = models.IntegerField() # year the book was published
    author = models.ForeignKey(Author, on_delete=models.CASCADE ,related_name='books')
    # The ForeignKey establishes a one-to-many relationship.

    def __str__(self):    
        return self.title