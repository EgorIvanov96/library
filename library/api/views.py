from djoser.views import UserViewSet
from rest_framework import viewsets

from users.models import User
from models.models import Books
from .serializers import UserSerializer, BooksSerializer, BookSerializer


class UserViewSet(UserViewSet):
    """Вьюсет для пользователей и авторов."""
    queruet = User.objects.all()
    serializer_class = UserSerializer


class BooksViewSet(viewsets.ModelViewSet):
    """Вьюсет для книг."""
    queryset = Books.objects.all()
    # serializer_class = BooksSerializer

    def get_serializer_class(self):
        if self.action in 'list':
            return BookSerializer
        return BooksSerializer
