from functools import reduce


def luhn(card_numb):

    numbers = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    card_numb = reduce(str.__add__, filter(str.isdigit, card_numb))
    evens = sum(int(i) for i in card_numb[-1::-2])
    odds = sum(numbers[int(i)] for i in card_numb[-2::-2])
    return (evens + odds) % 10 == 0


card_numb = input('Enter card number:')
while True:
    if card_numb == " ":
        print('Do not enter empy string. Try again!')
        break

    else:
        print('Card is valid: ', luhn(card_numb))
        break
