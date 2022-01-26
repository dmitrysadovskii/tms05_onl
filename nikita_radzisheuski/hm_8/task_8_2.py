
"""Creating dictionary. Keys are integer numbers that will be used for comparing
 with entered numbers. This dict will be sorted by values.
"""
dictionary_of_nums = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                      7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
                      13: 'thirty', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
                      18: 'eighteen', 19: 'nineteen'}


def sort_numbers(take_function):
    """Creating function for sorting entered numbers. We wrap nums using dictionary of nums"""
    def wrap_function(numbers):
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])

        names_in_english = []
        for num in numbers:
            if num in dictionary_of_nums:
                names_in_english.append(dictionary_of_nums[num])

        names_in_english = sorted(names_in_english)

        for name in names_in_english:
            for i in dictionary_of_nums:
                if dictionary_of_nums[i] == name:
                    print(i, end=' ')
    return wrap_function


@sort_numbers
def print_sorting_numbers(user_numbers):
    print(user_numbers)


print_sorting_numbers(input("Enter numbers separated by spacing: ").split())
