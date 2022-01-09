number = 3219
new_number = input('Введите четырехзначное число: ')
new_number_list = list(new_number)
number_list = list(str(number))

bik = 0
korova = 0
unique = set(new_number_list)


if len(new_number_list) == 0:
    print('Вы ничего не ввели!')
else:
    if len(new_number_list) != 4:
        print('Вы ввели не четырехзначное число!')
    elif len(set(number_list)) != len(unique):
        print('Цыфры не должны повторяться!')
    else:
        for i in number_list:
            if i in new_number_list:
                if number_list.index(i) == new_number_list.index(i):
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
