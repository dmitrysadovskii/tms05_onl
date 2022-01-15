number_names = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
    5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
    16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


def decorator(func):
    def wrapper(args):
        arr_int = []
        arr_names = []
        args = args.split()
        for i in args:
            arr_int.append(int(i))
        for i in arr_int:
            arr_names.append(number_names[i])
        arr_names = sorted(arr_names)
        return func(arr_names)

    return wrapper


@decorator
def sort_number_names(arr_names: list):
    arr_keys = []
    for i in arr_names:
        if i in list(number_names.values()):
            arr_keys.append(list(number_names.values()).index(i))
    return arr_keys


def string_validation(user_input: str) -> bool:
    user_input_int = []
    for k in user_input:
        if k in '0123456789 ':
            pass
        else:
            print('Строка содержит не только положительные числа и пробелы')
            return False
    user_input = user_input.split()
    if len(user_input) > 100:
        print('Количество чисел последовательности не должно быть больше 100')
        return False
    elif len(user_input) == 0:
        print('Вы ввели пустую строку')
        return False
    for i in user_input:
        user_input_int.append(int(i))
    for n in user_input_int:
        if not 0 <= n <= 19:
            print('Каждое число последовательности должно быть от 0 до 19')
            return False
    return True


while True:
    user_input = input('Введите последовательность чисел: ')
    is_valid = string_validation(user_input)
    if not is_valid:
        continue
    else:
        print(sort_number_names(user_input))
    break
