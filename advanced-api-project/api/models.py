from django.db import models

# Create your models here.
class Author(models.Model):
    """model for authors"""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    """model for books by author"""
    title = models.CharField(max_length=100) # title of the book
    publication_year = models.IntegerField() # year of the book publication
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books') # the foreighn key establishing a one to many relationship

    def __str__(self):
        return self.title
    