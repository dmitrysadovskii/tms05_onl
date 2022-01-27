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
    def __init__(self, book_name, author, pages_quantity,
                 isbn, flag, reserved):
        self.book_name = book_name
        self.author = author
        self.pages_quantity = pages_quantity
        self.isbn = isbn
        self.flag = flag
        self.reserved = reserved
        Book.books_count += 1


book_1 = Book("Neznayka", "Somebody", 505, 978-3-16-148410-0, "BY", False)
book_2 = Book("A Byte of Python", "Swaroop C H", 164, 978-5-16-122410-0,
              "US", False)
book_3 = Book("Pobeg", "Somebody Else", 404, 922-3-16-148110-0, "EU", False)
print(Book.books_count)


class User:
    def get_book(self):
        pass

    def return_book(self):
        pass

    def book_a_book(self):
        pass
