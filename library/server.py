import grpc
from concurrent import futures
import books_pb2
import books_pb2_grpc
# from django.conf import settings
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library.settings')
django.setup()

from reviews.models import Books
# from users.models import User  # Импортируй ваши модели


class BooksService(books_pb2_grpc.BooksServiceServicer):

    def GetBookById(self, request, context):
        # Получаем книгу по id
        try:
            book = Books.objects.get(id=request.id)
            return books_pb2.Book(
                id=book.id,
                name_book=book.name_book,
                author=book.author.username,
                date_publication=str(
                    book.date_publication.strftime('%H:%M %d %B %Y')
                    )
            )
        except Books.DoesNotExist:
            context.set_details('Книга не найдена.')
            context.set_code(grpc.StatusCode.NOT_FOUND)
            return books_pb2.Book()

    def ListAllBooks(self, request, context):
        # Получаем все книги
        books = Books.objects.all()
        response = books_pb2.GetAllBooksResponse()
        for book in books:
            response.books.add(
                # id=book.id,
                name_book=book.name_book,
                # author=book.author.username,
                # date_publication=str(book.date_publication)
            )
        return response


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    books_pb2_grpc.add_BooksServiceServicer_to_server(BooksService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC сервер запущен на порту 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
    django.setup()
    serve()
