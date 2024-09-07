from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer: Serializes all fields in the Book model, with custom validation for the publication_year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure the publication year is not in the future
    def validate_publication_year(self, value):
        if value > datetime.now().year:
            raise serializers.ValidationError("The publication year cannot be in the future.")
        return value


# AuthorSerializer: Serializes the Author model, and includes nested BookSerializer to serialize related books.
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to include books related to the author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
