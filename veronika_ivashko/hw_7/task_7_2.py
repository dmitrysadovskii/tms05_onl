"""
1) Напишите генератор который принимает список
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и возвращает новый
список только с положительными числами.
"""


def get_positive_numbers(input_numbers: list) -> list:
    """
    Filter only positive numbers from the input list.
    :param input_numbers: input list of numbers to filter.
    :return: list of numbers greater than zero.
    """
    return [num for num in input_numbers if num > 0]


print(get_positive_numbers([34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]))
