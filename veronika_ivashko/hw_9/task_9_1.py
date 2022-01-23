"""
    1. Библиотека
Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
зарезервирована ли книги или нет. Создайте класс пользователь который может
брать книгу, возвращать, бронировать. Если другой пользователь хочет взять
зарезервированную книгу(или которую уже кто-то читает - надо ему про это
сказать).
"""


class Book:

    all_books = []

    def __init__(self, name: str, author: str, num_pages: int, isbn: int,
                 is_reserved=0, is_taken=0):
        self.name = name
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = is_reserved
        self.is_taken = is_taken
        Book.all_books.append(self)


class Visitor:

    total_visitors = 0
    all_visitors = []

    def __init__(self, name: str, id_number=total_visitors + 1):
        self.name = name
        self.id_number = id_number
        self.books_reserved = []
        self.books_taken = []
        Visitor.all_visitors.append(self)

    def reserve_book(self, book: Book):
        """
        Check if book is not reserved yet and is not taken, then reserve it
        and add to the list of reserved books by certain visitor.
        :param book: object of class Book that visitor wants to reserve.
        :return: None.
        """
        if book.is_reserved == 0 and book.is_taken == 0:
            book.is_reserved = 1
            self.books_reserved.append(book)
            print(f'Book {book.name} was reserved by {self.name}.')
        else:
            print(f'Sorry the book {book.name} is not available now, please'
                  f' choose another.')

    def get_book(self, book: Book):
        """
        Check if book is available for taking it - already is in reserved list
        of the visitor or is available for anyone else, if it is free then give
        it to visitor, update flags for the book and add the book to the list
        of taken books for the visitor, remove from list of reserved books if
        it was there.
        :param book: object of class Book that visitor wants to take.
        :return: None.
        """
        # was not reserved and is not available now
        if book not in self.books_reserved \
                and (book.is_reserved == 1 or book.is_taken == 1):
            print(f'Sorry book {book.name} can not be taken')
            return
        # was already reserved
        elif book in self.books_reserved:
            self.books_reserved.remove(book)
        # for reversed and non-reserved but available books:
        book.is_reserved = 0
        book.is_taken = 1
        self.books_taken.append(book)
        print(f'You have got the book {book.name}.')

    def return_book(self, book: Book):
        """
        Check if book was taken by the visitor, if it was then return the book
        by updating the flag of the book and removing it from the list of taken
        books by this visitor.
        :param book: object of class Book that visitor wants to return.
        :return: None.
        """
        if book in self.books_taken:
            self.books_taken.remove(book)
            book.is_taken = 0
            print(f'Book {book.name} was returned by {self.name}.')
        else:
            print(f'You did not get the book {book.name}.')

