from book import Book
from database_connection import DatabaseConnection

class BookRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row['title'], row['author'], row['id'])
            books.append(item)

        return books

    def create(self, book):
            self.connection.execute('INSERT INTO books (title, author) VALUES (%s, %s)', [book.title, book.author])
            return None

    # def find(self, book_id):
    #     rows = self._connection.execute(
    #         'SELECT * from books WHERE id = %s', [book_id])
    #     row = rows[0]
    #     return Book(row["id"], row["title"], row["author"])

    

    # def delete(self, book_id):
    #     self._connection.execute(
    #         'DELETE FROM books WHERE id = %s', [book_id])
    #     return None