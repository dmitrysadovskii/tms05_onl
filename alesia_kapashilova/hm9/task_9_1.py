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

    def book_to_take(self, us_book):
        self.books.append(us_book)

    def take_book(self):
        for us_book in self.books:
            if us_book.taken not in self.books and us_book.reserved == 0:
                print(f'You have taken {us_book.book}.')
                us_book.taken += 1
            elif us_book.taken == 0 and us_book.reserved != 0:
                print(f'{us_book.book} has already reserved. '
                      f'Please choose another book to take.')
            elif us_book.taken != 0:
                print(f'{us_book.book} has already taken. '
                      f'Please choose another book to take.')

    def reserve_book(self):
        for us_book in self.books:
            if us_book.taken == 0 and us_book.reserved == 0:
                print(f'You have reserved {us_book.book}.')
                us_book.reserved += 1
            elif us_book.taken != 0 and us_book.reserved == 0:
                print(f'{us_book.book} has already taken. '
                      f'Please choose another book to reserve.')
            elif us_book.reserved != 0:
                print(f'{us_book.book} has already reserved. '
                      f'Please choose another book to reserve.')

    def return_book(self):
        for us_book in self.books:
            if us_book.taken == 1:
                us_book.taken = 0
                print(f'Thank you for bringing back {us_book.book}')


book1 = Book('11/22/63', 'Стивен Кинг', 800, 0 - 586 - 63795 - 5, 0, 0)
book2 = Book('Тьма между нами', 'Джон Марс', 320, 1 - 55404 - 295 - 7, 0, 0)
User1 = User()
User1.book_to_take(book1)
User1.take_book()
User2 = User()
User2.book_to_take(book1)
User2.reserve_book()
