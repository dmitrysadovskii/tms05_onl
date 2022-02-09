"""
Лексикографическое возрастание
На вход подаётся некоторое количество (не больше сотни) разделённых пробелом
целых чисел (каждое не меньше 0 и не больше 19).
Выведите их через пробел в порядке лексикографического возрастания названий
этих чисел в английском языке.
Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, поскольку
слово two в словаре встречается позже слова three, а слово three -- позже
слова one (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является
истинным)
number_names =
{
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven',
    12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'
}
"""


def sort_numbers_decorator(func):
    """
    For a string of numbers space-separated return string of these numbers
    sorted according to their names alphabetically.
    Only numbers less or equal to 19 can be used.
    :param func: function to which the decorator will be applied.
    :return: result of specified function.
    """
    def wrapper(some_str):
        number_names = {
            0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen'
        }
        numbers = list(number_names.keys())
        names = list(number_names.values())
        args = [el for el in some_str.split()]
        if all(arg.isdigit() and 0 <= int(arg) <= 19 for arg in args):
            number_names_sorted = sorted([number_names.get(int(arg))
                                          for arg in args])
            numbers_sorted = [str(numbers[names.index(name)])
                              for name in number_names_sorted]
            new_str = ' '.join(numbers_sorted)
            func(new_str)
        else:
            print('Please enter only positive integers less or equal to 19.')
    return wrapper


@sort_numbers_decorator
def display_numbers(num_str):
    print(num_str)


display_numbers('1 5 9 2 18')
display_numbers('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19')
display_numbers('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20')
display_numbers('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 -2')
display_numbers('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 f')
display_numbers('0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 2.5')
