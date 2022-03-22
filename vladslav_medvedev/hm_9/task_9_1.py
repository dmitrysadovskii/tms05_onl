"""
Библиотека Library
Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
зарезервирована ли книги или нет. Создайте класс пользователь который может
брать книгу, возвращать, бронировать. Если другой пользователь хочет взять
зарезервированную книгу(или которую уже кто-то читает
- надо ему про это сказать).
"""


class Book:
    all_books = []

    def __init__(self, name: str, author: str, number_pages: int, isbn: int,
                 reserved=0, taken=0):
        self.name = name
        self.author = author
        self.number_pages = number_pages
        self.isbn = isbn
        self.reserved = reserved
        self.taken = taken
        Book.all_books.append(self)


class User:
    total_users = 0
    all_users = []

    def __init__(self, name: str, id=total_users + 1):
        self.name = name
        self.id = id
        self.book_reserved = []
        self.book_taken = []
        User.all_users.append(self)

    def reserve_book(self, book: Book):
        if book.reserved == 0 and book.taken == 0:
            book.reserved = 1
            self.books_reserved.append(book)
            print(f'Book {book.name} is reserved by {self.name}')
        else:
            print(f'Sorry the book {book.name} is unvaliable now')

    def get_book(self, book: Book):
        if book not in self.book_reserved and book.reserved == 1 \
                or book.taken == 1:
            print(f'Sorry book {book.name} u cant be taken')
            return
        elif book in self.book_reserved:
            self.book_reserved.remove(book)
        book.reserved = 0
        book.taken = 1
        self.book_taken.append(book)
        print(f'U have got the book {book.name}')

    def come_back(self, book: Book):
        if book in self.book_taken:
            self.book_taken.remove(book)
            book.is_taken = 0
            print(f'Book {book.name} was come back by {self.name}')
        else:
            print(f'U didnt get the book {book.name}')
