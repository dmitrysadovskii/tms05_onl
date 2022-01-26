"""HOMEWORK TASK NUMBER ONE
THIS CODE IS A CREDIT CARD VALIDITY
CHECK USING LUNA ALGORITHM
"""

from functools import reduce

"""Checking if the entered number is integer"""
while True:
    try:
        enter_cc_creds = str(int(input("Enter CC number: ")))
        if len(enter_cc_creds) > 10:
            break
    except ValueError:
        print("You must enter valid CC number, not letters or spaces.")

"""Function using algorithm louna to check Credit card number validity"""


def louna(enter_cc_creds):
    lookup = (0, 2, 4, 6, 8, 1, 3, 5, 7, 9)
    enter_cc_creds = reduce(str.__add__, filter(str.isdigit, enter_cc_creds))
    evens = sum(int(i) for i in enter_cc_creds[-1::-2])
    odds = sum(lookup[int(i)] for i in enter_cc_creds[-2::-2])
    return (evens + odds) % 10 == 0


def results_printing(louna, valid_cc):
    if louna(valid_cc) is True:
        print('The entered CC is Valid')
    else:
        print('You entered the wrong CC number')


louna(enter_cc_creds)
results_printing(louna, enter_cc_creds)
