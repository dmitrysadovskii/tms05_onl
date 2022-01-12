def validate(card_number):
    if len(str(card_number)) < 11 or len(str(card_number)) > 16:
        return print('Номер должен состоять либо из более 10 '
                     'либо из менее 20 цифр')
    elif set(str(card_number)) <= set('0123456789'):
        array = []
        for i in str(card_number):
            array.append(int(i))
        if len(str(card_number)) % 2 == 0:
            for x in range(0, len(str(card_number)), 2):
                array[x] = array[x] * 2
                if array[x] > 9:
                    array[x] = array[x] - 9
                else:
                    continue
        else:
            for x in range(1, len(str(card_number)), 2):
                array[x] = array[x] * 2
                if array[x] > 9:
                    array[x] = array[x] - 9
                else:
                    continue
        if sum(array) % 10 == 0:
            print('Номер карты ввалидный')
        else:
            print('Номер карты неввалидный')
    else:
        print('Некорректно введены данные')


validate('76009244561')
