"""Создайте класс book с именем книги, автором, кол-м страниц, ISBN,
флагом, зарезервирована ли книги или нет. Создайте класс пользователь
который может брать книгу, возвращать, бронировать.
Если другой пользователь хочет взять зарезервированную книгу
(или которую уже кто-то читает - надо ему про это сказать).
"""


class Book:
    """Class attribute for counting books"""
    books_count = 0
    """Creating class methods"""
    def add_new_book(self, book_name, author, pages_quantity, isbn, flag, reserved):
        self.book_name = book_name
        self.author = author
        self.pages_quantity = pages_quantity
        self.isbn = isbn
        self.flag = flag
        self.reserved = reserved


class User:
    def get_book(self):
        pass
