import grpc
import books_pb2
import books_pb2_grpc


def run():
    # Подключаемся к серверу
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = books_pb2_grpc.BooksServiceStub(channel)

        # Пример запроса на получение книги по ID
        book_id = 4  # измените на тот ID, который у вас есть
        response = stub.GetBookById(books_pb2.GetBookRequest(id=book_id))
        print(f'Книга: {response.name_book}, '
              f'Автор: {response.author}, '
              f'Дата публикации: {response.date_publication}')

        # Пример запроса на получение всех книг
        all_books_response = stub.ListAllBooks(books_pb2.ListAllBooksRequest())
        for book in all_books_response.books:
            print(f'{book.name_book}')


if __name__ == '__main__':
    run()
