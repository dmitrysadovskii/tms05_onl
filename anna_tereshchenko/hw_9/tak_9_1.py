from enum import Enum


class BookStatuses(Enum):
    Available = 1
    Taken = 2
    Booked = 3


class Book:
    def __init__(self, book_name, author,
                 number_of_pages, isbn, status: BookStatuses):
        self.book_name = book_name
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.status = status
        self.user: User = None


class User:
    def __init__(self, name):
        self.name = name
        self.books = []

    def take_book(self, book: Book):
        if book.status == BookStatuses.Available:
            book.status = BookStatuses.Taken
            self.books.append(book)
            book.user = self
            print(f'The {book.book_name} book have been taken by {self.name}')
        else:
            print(f'The {book.book_name} book is taken or reserved by '
                  f'{book.user and book.user.name or "No username"}')

    def reserve_book(self, book: Book):
        if book.status == BookStatuses.Available:
            book.status = BookStatuses.Taken
            self.books.append(book)
            print(f'The {book.book_name} book have been reserved by '
                  f'{self.name}')
        else:
            print(f'The {book.book_name} book is taken or reserved')

    def return_book(self, book: Book):
        if book in self.books:
            book.status = BookStatuses.Available
            self.books.remove(book)
            print(f'The {book.book_name} book has been returned')
        else:
            print('You didn"t take or reserve this book')


book1 = Book('1984', 'George Orwell', 328, 'ISBN_1', BookStatuses.Available)
book2 = Book('Fahrenheit 451', 'Ray Bradbury',
             256, 'ISBN_2', BookStatuses.Available)
user1 = User('Anna')
user1.take_book(book2)
user2 = User('Dima')
user2.take_book(book2)
user1.return_book(book2)
