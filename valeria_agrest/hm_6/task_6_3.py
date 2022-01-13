def calculator():
    print("Выберите действие, которое хотите сделать:\n"
          "1.Сложение\n"
          "2.Вычитание\n"
          "3.Умножение\n"
          "4.Деление\n")
    options = ('1', '2', '3', '4')
    user_option = input("Введите номер пункта меню:")
    if user_option not in options:
        print('Введите только пункт меню от 1 до 4!')
    else:
        x = float(input("Введите первое число:"))
        y = float(input("Введите второе число:"))
        if user_option == '1':
            print(x + y)
        elif user_option == '2':
            print(x - y)
        elif user_option == '3':
            print(x * y)
        elif user_option == '4':
            if y == 0:
                print("На ноль делить нельзя!")
            elif y != 0 and x % y == 0:
                print(x / y)
            elif y != 0 and x % y != 0:
                division = x / y
                str_division = str(division)
                quotient = str_division.split(".")[0]
                remainder = str_division[str_division.find(".") + 1:]
                remainder_1 = remainder[0]
                print(f"Частное: {quotient}, остаток: {remainder_1}")


while True:
    calculator()
