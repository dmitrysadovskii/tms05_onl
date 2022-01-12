number = 3219
new_number = input('Введите четырехзначное число: ')
number_str = str(number)

bik = 0
korova = 0
unique = set(list(new_number))


if len(new_number) == 0:
    print('Вы ничего не ввели!')
else:
    if not new_number.isdigit():
        print('Введите только цыфры!')
    elif len(new_number) != 4:
        print('Вы ввели не четырехзначное число!')
    elif len(set(number_str)) != len(unique):
        print('Цыфры не должны повторяться!')
    else:
        for i in number_str:
            if i in new_number:
                if number_str.index(i) == new_number.index(i):
                    bik += 1
                else:
                    korova += 1

        answer = ''

        if bik > 0 or korova > 0:
            if korova == 1:
                answer += 'Одна корова'
            elif korova == 2:
                answer += 'Две коровы'
            elif korova == 3:
                answer += 'Три коровы'
            elif korova == 4:
                answer += 'Четыре коровы'

            if len(answer) > 0 and 0 < bik < 4:
                answer += ', '

            if bik == 1:
                answer += 'один бык'
            elif bik == 2:
                answer += 'два быка'
            elif bik == 3:
                answer += 'три быка'
            elif bik == 4:
                answer += 'Вы победили!'

            print(answer)

        else:
            print('Мимо!')
