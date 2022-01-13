def only_numbers(num: str) -> bool:
    if num == '':
        print('Вы ничего не ввели!')
        return False
    else:
        return num.isdigit()


def logic(array, el):
    res = 0
    if el * 2 > 9:
        res = el * 2 - 9
    else:
        res = el * 2
    array.append(res)
    return True


def validation(card_number):
    card_number_list = []
    modify_list = []
    sum_card_number_list = 0

    for el in card_number:
        card_number_list.append(int(el))

    control_num = card_number_list[-1]
    card_number_list.pop(-1)
    even = card_number_list[1::2]
    odd = card_number_list[0::2]

    if len(card_number_list) % 2 == 0:
        for el in even:
            logic(modify_list, el)
        sum_card_number_list = sum(modify_list) + sum(odd)
    elif len(card_number_list) % 2 != 0:
        for el in odd:
            logic(modify_list, el)
        sum_card_number_list = sum(modify_list) + sum(even)

    sum_numbers = sum_card_number_list + control_num

    if sum_numbers % 10 == 0:
        return True
    else:
        return False


while True:
    card_input = input('Введите номер карты: ')
    just_numbers = only_numbers(card_input)
    if just_numbers:
        valid_or_invalid = validation(card_input)
        if valid_or_invalid:
            print('Valid')
            break
        else:
            print('Invalid')
