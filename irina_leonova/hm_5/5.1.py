while True:
    a = input("Загаданное число: ")
    if a.isdigit():
        var = True
    else:
        print("Вводите только числа, без пробелов")
        continue
    set_a = set(a)
    if len(a) == len(set_a):
        break
    else:
        print("Есть одинаковые")
while True:
    b = input("Ваше число: ")
    if b.isdigit():
        var = True
    else:
        print("Вводите только числа,без пробелов")
        continue
    c = 0
    k = 0
    for i in range(0, 4):
        if b[i] == a[i]:
            c += 1
        if b[i] != a[i]:
            for j in a:
                if b[i] == j:
                    k += 1
    print("быков: ", c)
    print("коров: ", k)
    if c == 4:
        print("Победа!")
        break
