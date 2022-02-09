class Book:
    def __init__(self, book, writer, pages, isbn, reserve, taken):
        self.book = book
        self.writer = writer
        self.pages = pages
        self.isbn = isbn
        self.reserve = reserve
        self.taken = taken


class Reader:
    def __init__(self):
        self.books = list()

    def book_to_take(self, correct_book):
        self.books.append(correct_book)

    def take_book(self):
        for correct_book in self.books:
            if correct_book.taken not in self.books and correct_book.reserve == 0:
                print(f'You take {correct_book.book}.')
                correct_book.taken += 1
            elif correct_book.taken == 0 and correct_book.reserve != 0:
                print(f'{correct_book.book} is reserved, choose another.')

    def reserve_book(self):
        for correct_book in self.books:
            if correct_book.taken == 0 and correct_book.reserve == 0:
                print(f'You reserved {correct_book.book}.')
                correct_book.reserve += 1
            elif correct_book.taken != 0 and correct_book.reserve == 0:
                print(f'{correct_book.book} already taken, choose another.')
            elif correct_book.reserve != 0:
                print(f'{correct_book.book} has already reserved, choose another.')

    def return_book(self):
        for correct_book in self.books:
            if correct_book.taken == 1:
                correct_book.taken = 0
                print(f' you for bring back {correct_book.book}')


test_book = Book('Cool book', 'N!_writer', 'isbn_1', 0, 0, 0)

Reader1 = Reader()
Reader1.book_to_take(test_book)
Reader1.take_book()
Reader2 = Reader()
Reader2.book_to_take(test_book)
Reader2.reserve_book()
