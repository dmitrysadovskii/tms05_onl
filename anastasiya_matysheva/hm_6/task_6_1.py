from functools import reduce
import re


def luhn(code):
    look_up = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    code = reduce(str.__add__, filter(str.isdigit, code))
    evens = sum(int(i) for i in code[-1::-2])
    odds = sum(look_up[int(i)] for i in code[-2::-2])
    return (evens + odds) % 10 == 0


def check_card():
    card_numb = input('Please, enter credit card number: ')
    opt = re.compile("[ -\\/:-@\\[-\\`{-~ \t]")

    if opt.search(card_numb):
        print('Please, enter credit card number'
              ' without space or special simbol')
    elif card_numb.islower():
        print('Please, enter only numbers')
    elif len(card_numb) > 16:
        print('Please, enter no more than 16 numbers')
    elif not card_numb:
        print('Please, enter credit card number')
    else:
        if luhn(card_numb):
            print('Credit card is valid')
        else:
            print('Credit card invalid')


check_card()
