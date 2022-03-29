isbn_book = []


def check_reserve(options, store, isbn):
    result = ''
    if len(store) == 0:
        options += 1
        store.append(isbn)
        result += "You have"
    else:
        if isbn in store:
            result += "should have a different ISBN, this one is used'"
        else:
            options += 1
            store.append(isbn)
            result += "You have"
    return result


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
        self.books = []

    def book_to_take(self, us_book):
        self.books.append(us_book)

    def take_book(self):
        for us_book in self.books:
            if us_book.taken == 0 in self.books and us_book.reserved != 0:
                print(f'{us_book.book} has already reserved. '
                      f'Please choose another book to take')
            elif us_book.taken != 0:
                print(f'{us_book.book} has already reserved. '
                      f'Please choose another book to take.')
            else:
                result = check_reserve(us_book.taken, isbn_book, us_book.isbn)
                if result == "You have":
                    print(f'{result} taken {us_book.book}')
                else:
                    print(f"{us_book.book} {result}")

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
            else:
                result = check_reserve(us_book.reserved, isbn_book,
                                       us_book.isbn)
                if result == 'You have':
                    print(f'{result} reserved {us_book.book}')
                else:
                    print(f"{us_book.book} {result}")

    def return_book(self):
        for us_book in self.books:
            if us_book.taken == 1:
                us_book.taken = 0
                isbn_book.remove(us_book.isbn)
                print(f'Thank you for bringing back {us_book.book}')
