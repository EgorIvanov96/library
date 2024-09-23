from rest_framework import serializers

from users.models import User
from models.models import Books


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email', 'username',)


class BookSerializer(serializers.ModelSerializer):
    """Сериалалайзер для представления списка книг."""

    class Meta:
        model = Books
        fields = ('name_book',)


class BooksSerializer(serializers.ModelSerializer):
    """Сериалайзер для книг."""
    author = UserSerializer(read_only=True)

    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        author = self.context['request'].user
        books = Books.objects.create(author=author, **validated_data)
        return books
