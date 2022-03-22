while True:
    number = input("Введите-номер-карты:")
    number = number.replace(" ", "")
    if number == "":
        print("exist line, pls enter card")
        continue
    if len(number) not in range(13, 17):
        print("Check the number of characters")
        continue
    if number.isdigit():
        var = True
    else:
        print("Enter only numbers")
        continue
    number_Luhn = 0
    b_numbers = 0
    s_numbers = 0
    sum_other = 0
    if len(number) % 2 == 0:
        for i in range(0, len(number), 2):
            if (2 * int(number[i])) > 9:
                b_numbers = b_numbers + (2 * int(number[i])) - 9
            if (2 * int(number[i])) <= 9:
                s_numbers = s_numbers + (2 * int(number[i]))
        for e in range(1, len(number), 2):
            sum_other = sum_other + int(number[e])
            number_Luhn = b_numbers + s_numbers + sum_other
        if number_Luhn % 10 == 0:
            print("Прошел проверку: ", number)
            break
        else:
            print(False)
            continue
    if len(number) % 2 != 0:
        len_1 = len(number) - 1
        for b in range(1, len_1, 2):
            if (2 * int(number[b])) > 9:
                b_numbers = b_numbers + (2 * int(number[b])) - 9
            if (2 * int(number[b])) <= 9:
                s_numbers = s_numbers + (2 * int(number[b]))
        for c in range(0, len_1, 2):
            sum_other = sum_other + int(number[c])
            number_Luhn = b_numbers + s_numbers + sum_other + int(number[-1])
        if number_Luhn % 10 == 0:
            print("Прошел проверку: ", number)
            break
        else:
            print(False)
            continue
