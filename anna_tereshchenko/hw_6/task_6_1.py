def luna_algorithm(card_number) -> bool:
    arr = []
    for i in card_number:
        arr.append(int(i))
    control_number = arr[-1]
    arr.pop(len(arr) - 1)
    if len(arr) % 2 == 0:
        start_position = 1
    else:
        start_position = 0
    while start_position < len(arr):
        if arr[start_position] * 2 > 9:
            arr[start_position] = arr[start_position] * 2 - 9
        else:
            arr[start_position] = arr[start_position] * 2
        start_position += 2
    arr_sum = sum(arr) + control_number
    if arr_sum % 10 == 0:
        return True
    else:
        return False


def validate_user_input(user_input: str) -> bool:
    if len(user_input) > 0:
        for k in user_input:
            if k not in '0123456789':
                print('Вы ввели не число')
                return False
    else:
        print('Вы ничего не ввели')
        return False
    return True


k = 0
print('Номер карты должен содержать только цифры без пробелов\n'
      'У вас есть три попытки ввести корректный номер карты')
while k < 3:
    card_number_input = (input('Введите номер карты: '))
    is_valid = validate_user_input(card_number_input)
    if not is_valid:
        k += 1
        if k == 3:
            pass
        else:
            print(f'Количество оставшихся попыток: {3 - k} из 3')
        continue
    else:
        result = luna_algorithm(card_number_input)
        if result:
            print('Карта валидна')
        else:
            print('Карта не валидна')
    break
