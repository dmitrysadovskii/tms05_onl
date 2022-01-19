number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


def sorter(func):
    def wrapper(numbers):
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])

        names = []
        for i in numbers:
            if i in number_names:
                names.append(number_names[i])
        names = sorted(names)

        for i in names:
            for j in number_names:
                if number_names[j] == i:
                    print(j, end=' ')

    return wrapper


@sorter
def show_sorter_numbers(numbers):
    print(numbers)


numbers = input("Введите числа для сортировки через пробел: ").split()
show_sorter_numbers(numbers)
