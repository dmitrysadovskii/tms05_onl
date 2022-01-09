'''
При совпадении чисел:
1 - Совпадение по значению и индексу - одна корова
2 - Не совпадение по значению и индексу - один бык
3 - Если совпали все 4 - то ты "Победил!!!"
Цель игры - собрать 4 коровы!
'''
const = '3219'
for i in range(100):
    n, count_c, count_b = 0, 0, 0
    user_input = input('Введите 4х значное число: ')
    count_user_input = len(user_input)
    for i in range(1):
        if count_user_input > 0 or count_user_input < 4\
                or count_user_input != '' or not count_user_input.isdigit():
            print('Значение введено неверно! Повторите повытку!')
    break
    for i in const:
        if i == user_input[n]:
            count_c += 1
            n += 1
        elif i != user_input[n]:
            count_b += 1
            n += 1
    if count_c > 3:
        print("Ураааа ты победил ")
        break
    else:
        print(f'Кол-во Коров:{count_c}')
        print(f'Кол-во Быков:{count_b}')
'''
Правила немного изменились
пс на написание этой игры ушло много часов
'''
