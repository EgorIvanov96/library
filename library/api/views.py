from djoser.views import UserViewSet
from rest_framework import viewsets
import pika
import json

from users.models import User
# from models.models import Books
from reviews.models import Books
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

    def perform_create(self, serializer):
        serializer.save()
        # Send a message to RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='books_queue')
        channel.basic_publish(exchange='', routing_key='books_queue', body='message')
        connection.close()

    """def send_message(action, book_id=None):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        channel.queue_declare(queue='book_actions')

        message = json.dumps({'action': action, 'book_id': book_id})
        channel.basic_publish(exchange='', routing_key='book_actions', body=message)
        connection.close()"""
