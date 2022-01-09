def luna_algorithm(card_number):
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


while True:
    try:
        card_number_input = (input('Введите номер карты: '))
        int_card_number = int(card_number_input)
        result = luna_algorithm(card_number_input)
        if result:
            print('Карта валидна')
        else:
            print('Карта не валидна')
        break
    except ValueError:
        print('Это не число, введите число, содержащее только цифры')
        continue
