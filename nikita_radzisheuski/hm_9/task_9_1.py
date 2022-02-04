"""Создайте класс book с именем книги, автором, кол-м страниц, ISBN,
флагом, зарезервирована ли книги или нет. Создайте класс пользователь
который может брать книгу, возвращать, бронировать.
Если другой пользователь хочет взять зарезервированную книгу
(или которую уже кто-то читает - надо ему про это сказать).
"""


class Book:
    """Class methods containing characteristics and statuses of the book"""

    def __init__(self, book, author, pages, isbn, flag, reserved, taken):
        self.book = book
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.flag = flag
        self.reserved = reserved
        self.taken = taken


class Guest:
    def __init__(self):
        self.books = list()

    def book_to_take(self, book):
        self.books.append(book)

    def get_book(self):
        for book in self.books:
            if book.taken not in self.books and book.reserved is False:
                print(f'You took <{book.book}>.')
                book.taken = True
            elif book.taken is False and book.reserved is True:
                print(f'<{book.book}> is reserved by other person')
            elif book.taken:
                print(f'<{book.book}> is taken by other person')

    def book_a_book(self):
        for book in self.books:
            if book.taken is False and book.reserved is False:
                print(f'You reserved <{book.book}>.')
                book.reserved = True
            elif book.taken is True and book.reserved is not True:
                print(f'<{book.book}> is taken by other person')
            elif book.reserved:
                print(f'<{book.book}> is reserved by other person')

    def return_book(self):
        for book in self.books:
            if book.taken:
                book.taken = False
                print(f'You returned <{book.book}>')


book1 = Book('Neznayka', 'Steven King', 505, "978-3-16-148410-0",
             'EU', False, False)
book2 = Book("A Byte of Python", "Swaroop C H", 164, "978-5-16-122410-0",
             "USA", False, False)
Guest1 = Guest()
Guest2 = Guest()
Guest3 = Guest()

Guest1.book_to_take(book1)
Guest1.get_book()
Guest2.book_to_take(book1)
Guest2.book_a_book()
Guest3.book_to_take(book2)
Guest3.book_a_book()
