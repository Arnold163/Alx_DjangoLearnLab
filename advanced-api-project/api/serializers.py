from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


class AuthorSerializer(serializers.ModelSerializer):
    """serializer for the book"""
    class Meta:
        model = Author
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """pub year not in the future"""
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        
class AuthorSerializer(serializers.ModelSerializer):
    """serial for the author model nested BookSerializers"""
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ['id', 'title', 'publication_year', 'author']
        
    

