from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class Bookserializer(serializers.ModelSerializer):
    class Meta:
        model = Book 
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """validate the publication year not in future"""
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    
class AuthorSerializer(serializers.ModelSerializer):
    """serializer for the Author model with nested BookSerializer"""
    books = Bookserializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'book']

    
