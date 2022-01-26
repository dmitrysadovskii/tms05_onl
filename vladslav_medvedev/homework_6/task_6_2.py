'''
На вход подается строка, например, "cccbba" результат работы программы
- строка “c3b2a"
Примеры для проверки работоспособности:
"cccbba" == "c3b2a1"
"abeehhhhhccced" == "a1b1e2h5c3e1d1"
"aaabbceedd" == "a3b2ce2d2"
"abcde" == "abcde"
"aaabbdefffff" == "a3b2def5"
'''
message = str(input("Please, write sting: "))
count = 1
x = 1
j = message[x:x + 1]
for i in message:
    if i in j:
        count += 1
    else:
        print(i, end='')
        print(count, end='')
        count = 1
    x += 1
    j = message[x:x + 1]
