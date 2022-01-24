def decorator(func):
    def wrapper(arg1):
        number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                        14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
        sorted_values = sorted(number_names.values())
        sorted_number_names = {}
        list_int_args = [int(i) for i in arg1.split(' ')]
        sorted_args = []
        for i in sorted_values:
            for k in number_names.keys():
                if number_names[k] == i:
                    sorted_number_names[k] = number_names[k]
                    break
        for k in sorted_number_names.keys():
            for i in list_int_args:
                if k == i:
                    sorted_args.append(i)
        list_str_args = [str(i) for i in sorted_args]
        print(' '.join(list_str_args))
        func(arg1)
    return wrapper


def valid_numbers(num: str):
    if not num:
        print('Вы ничего не ввели!')
        return False
    for i in num:
        if i not in '0123456789 ':
            print('Только положительные цифры и пробел')
            return False
    num_list = [int(i) for i in num.split(' ')]
    if len(num_list) > 100:
        print('Нельзя вводить более 100 чисел!')
        return False
    for i in num_list:
        if i > 19:
            print('Числа должны быть не меньше 0 и не больше 19!')
            return False
    else:
        return True


while True:
    user_input = input('Введите последовательность чисел: ')
    is_valid = valid_numbers(user_input)
    if not is_valid:
        continue
    else:
        function_decorated = decorator(valid_numbers)
        function_decorated(user_input)
        break
