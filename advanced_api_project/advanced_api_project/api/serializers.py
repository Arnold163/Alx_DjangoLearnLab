from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

class AuthorSerializer(serializers.ModelSerializer):
    # defines the Meta class which specifies the model to be used and the fields to be serialized
    class Meta:
        model = Author
        fields = ['id', 'title', 'publication_year', 'author']

        def validate_publication_year(self, value):

            current_year = datetime.now().year
            if value > current_year:
                raise serializers.ValidationError("Publication year cannot be in the future")
            return value

class BookSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['id', 'title', 'name', 'books']


