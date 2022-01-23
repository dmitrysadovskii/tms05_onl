class Book:

    def __init__(self, book, author, pages, isbn, reserved, taken):
        self.book = book
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved
        self.taken = taken


class User:

    def __init__(self):
        self.books = list()

    def book_to_take(self, a_book):
        self.books.append(a_book)

    def take_book(self):
        for a_book in self.books:
            if a_book.taken == 0 and a_book.reserved == 0:
                print(f'You have taken {a_book.book}.')
                a_book.taken += 1
            elif a_book.taken == 0 and a_book.reserved != 0:
                print(f'{a_book.book} has already reserved. '
                      f'Please choose another book to take.')
            elif a_book.taken != 0:
                print(f'{a_book.book} has already taken. '
                      f'Please choose another book to take.')

    def reserve_book(self):
        for a_book in self.books:
            if a_book.taken == 0 and a_book.reserved == 0:
                print(f'You have reserved {a_book.book}.')
                a_book.reserved += 1
            elif a_book.taken != 0 and a_book.reserved == 0:
                print(f'{a_book.book} has already taken. '
                      f'Please choose another book to reserve.')
            elif a_book.reserved != 0:
                print(f'{a_book.book} has already reserved. '
                      f'Please choose another book to reserve.')

    def bring_back_book(self):
        for a_book in self.books:
            if a_book.taken == 1:
                a_book.taken = 0
                print(f'Thank you for bringing back {a_book.book}')


book = Book('A Walk to Remember', 'Nicholas Sparks', 240, 'ISBN_1', 0, 0)
User1 = User()
User1.book_to_take(book)
User1.take_book()
User2 = User()
User2.book_to_take(book)
User2.reserve_book()
User1.bring_back_book()
User2.reserve_book()
