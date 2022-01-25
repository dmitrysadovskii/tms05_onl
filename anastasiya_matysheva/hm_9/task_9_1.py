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

    def take_a_book(self, booked):
        self.books.append(booked)

    def take_book(self):
        for booked in self.books:
            if booked.taken not in self.books and booked.reserved == 0:
                print(f'You have taken book {booked.book}.')
                booked.taken += 1
            elif booked.taken == 0 and booked.reserved != 0:
                print(f'{booked.book} is already reserved. '
                      f'Please choose another book.')
            elif booked.taken != 0:
                print(f'{booked.book} is already taken. '
                      f'Please choose another book.')

    def reserved(self):
        for booked in self.books:
            if booked.taken == 0 and booked.reserved == 0:
                print(f'You have reserved {booked.book}.')
                booked.reserved += 1
            elif booked.taken != 0 and booked.reserved == 0:
                print(f'{booked.book} is already taken. '
                      f'Please choose another book.')
            elif booked.reserved != 0:
                print(f'{booked.book} has already reserved. '
                      f'Please choose another book to reserve.')

    def return_the_book(self):
        for booked in self.books:
            if booked.taken == 1:
                booked.taken = 0
                print(f'Thank you for bringing back {booked.book}')


book1 = Book('"Flowers for Elgernon"', 'Keyes Daniel',
             358, 1 - 369 - 22129 - 7, 0, 0)
book2 = Book('"Night music"', 'Jojo Moyes', 400, 0 - 129 - 87963 - 2, 0, 0)
book3 = Book('"Fahrenheit 451"', 'Ray Bradbury',
             451, 1 - 666 - 2597 - 4, 0, 0)
user1 = User()
user1.take_a_book(book1)
user1.take_book()
user1.return_the_book()
user2 = User()
user2.take_a_book(book2)
user2.take_book()
user3 = User()
user3.take_a_book(book2)
user3.reserved()
user4 = User()
user4.take_a_book(book3)
user4.reserved()
user5 = User()
user5.take_a_book(book3)
user5.take_book()
user6 = User()
user6.take_a_book(book3)
user6.reserved()
