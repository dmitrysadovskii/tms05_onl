def luna_algorithm(card_number) -> bool:
    array = []
    for i in card_number:
        array.append(int(i))
    control_number = array[-1]
    array.pop(len(array) - 1)
    if len(array) % 2 == 0:
        start = 1
    else:
        start = 0
    while start < len(array):
        if array[start] * 2 > 9:
            array[start] = array[start] * 2 - 9
        else:
            array[start] = array[start] * 2
        start += 2
    array_sum = sum(array) + control_number
    if array_sum % 10 == 0:
        return True
    else:
        return False


def validate(user_card: str) -> bool:
    if len(user_card) > 0:
        for k in user_card:
            if k not in '0123456789':
                print('Это не число!')
                return False
    else:
        print('Ничего не введено!')
        return False
    return True


k = 0
print('Номер карты должен содержать только цифры без пробелов')
while k < 2:
    user_card_input = (input('Введите номер карты: '))
    is_valid = validate(user_card_input)
    if not is_valid:
        k += 1
        if k == 2:
            pass
        else:
            print(f'Последний шанс!')
        continue
    else:
        result = luna_algorithm(user_card_input)
        if result:
            print('Карта валидна')
        else:
            print('Карта не валидна')
    break
