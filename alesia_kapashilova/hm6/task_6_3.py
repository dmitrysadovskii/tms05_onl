a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))


def sum():
    global a, b
    print(f'Сумма чисел равна:  {a + b}')


def dif():
    global a, b
    print(f'Разность чисел равна:  {a - b}')


def mul():
    global a, b
    print(f'Произведение чисел равно:  {a * b}')


def div():
    global a, b
    if b == 0:
        print('На ноль делить нельзя!!!')
    else:
        print(f'Деление чисел равно:  {a / b}')


mydict = {1: sum, 2: dif, 3: mul, 4: div}
choices = list(map(int, input("Выберите операцию: \n1.Сложение \n2.Вычитание"
                              "\n3.Умножение \n4.Деление \n").split()))
for choice in choices:
    if 0 < choice < 5:
        mydict[choice]()
    else:
        print("That is not between 1 and 5! Try again:")
