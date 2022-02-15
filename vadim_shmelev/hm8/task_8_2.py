def decorator(func):
    def wrapper(arg1):
        numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                   5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                   10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                   14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                   17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
        sorted_numbers = sorted(numbers.values())
        sorted_number_names = {}
        list_int_args = [int(i) for i in arg1.split(' ')]
        sorted_args = []
        for i in sorted_numbers:
            for k in numbers.keys():
                if numbers[k] == i:
                    sorted_number_names[k] = numbers[k]
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
        print('You did nщt enter anything. Try again!')
        return False
    for i in num:
        if i not in '0123456789 ':
            print('Only positive numbers can be entered. Try again!')
            return False
    num_list = [int(i) for i in num.split(' ')]
    if len(num_list) > 100:
        print('You can enter no more than 100 numbers! Try again!')
        return False
    for i in num_list:
        if i > 19:
            print('You can enter numbers from 0 to 19! Try again!')
            return False
    else:
        return True


while True:
    user_input = input('Enter a sequence of numbers: ')
    is_valid = valid_numbers(user_input)
    if not is_valid:
        continue
    else:
        function_decorated = decorator(valid_numbers)
        function_decorated(user_input)
        break
