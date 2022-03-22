while True:
    print("Выберите операцию:")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    numbers = input("Введите номер пункта меню: ")
    if numbers.isdigit():
        var = True
    else:
        print("Проверьте указываемый пункт операции")
        continue
    numbers = int(numbers)
    if numbers not in range(0, 5):
        print("Проверьте указываемый пункт операции")
        continue
    number_1 = input("Введите первое число: ")
    if number_1.isdigit():
        var = True
    else:
        print("Проверьте указываемое число")
        continue
    number_1 = int(number_1)
    number_2 = input("Введите второе число:")
    if number_2.isdigit():
        var = True
    else:
        print("Enter only numbers")
        continue
    number_2 = int(number_2)
    if numbers == 1:
        print("Сумма: ", number_1 + number_2)
    if numbers == 2:
        print("Разница: ", number_1 - number_2)
    if numbers == 3:
        if number_1 != 0 and number_2 != 0:
            print("Произведение: ", number_1 * number_2)
        if number_1 == 0 or number_2 == 0:
            print("None")
    if numbers == 4:
        if number_1 != 0 and number_2 != 0:
            if number_1 % number_2 == 0:
                print("Частное: ", number_1 // number_2)
            else:
                print("Частное: ", round(number_1 / number_2) - 1,
                      ', Остаток: ', number_1 % number_2)
        if number_1 == 0 or number_2 == 0:
            print("None")
    break
