import random


def validate_user_input(user_input: str) -> bool:
    s = set()
    if len(user_input) > 0:
        for k in user_input:
            if k in '0123456789':
                s.add(k)
            else:
                print('Вы ввели не число')
                return False
    else:
        print('Вы ничего не ввели')
        return False
    if len(s) != len(user_input):
        print('Цифры не должны повторяться')
        return False
    if len(s) == 4:
        return True
    else:
        print('Вы ввели не четырехзначное число')
        return False


first = random.choice(range(1, 10))
leftover = list(range(0, 10))
leftover.remove(first)
random.shuffle(leftover)
secret = [first] + leftover[0:3]
bull = 0
digit_to_string = {0: 'ноль', 3: 'три', 4: 'четыре'}
digit_to_string_cow = {1: 'одна', 2: 'две'}
digit_to_string_cow.update(digit_to_string)
digit_to_string_bull = {1: 'один', 2: 'два'}
digit_to_string_bull.update(digit_to_string)
while bull != len(secret):
    bull = 0
    cow = 0
    answer = (input('Введите число: '))
    is_valid = validate_user_input(answer)
    if not is_valid:
        continue
    answer = [int(i) for i in answer]
    k = 0
    for i in answer:
        if i in secret:
            if secret[k] == answer[k]:
                bull += 1
            else:
                cow += 1
        k += 1
    if bull == 4:
        print('Вы выйграли')
        break
    if cow in (2, 3, 4):
        cow_str = 'коровы'
    elif cow == 1:
        cow_str = 'корова'
    else:
        cow_str = 'коров'
    if bull in (2, 3, 4):
        bull_str = 'быка'
    elif bull == 1:
        bull_str = 'бык'
    else:
        bull_str = 'быков'
    print(f'{digit_to_string_cow[cow]} {cow_str}, '
          f'{digit_to_string_bull[bull]} {bull_str}')
