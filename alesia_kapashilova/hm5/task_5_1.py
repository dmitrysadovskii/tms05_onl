from random import choice

range_num = '0123456789'
hidden_number = choice(range_num[0:10])
count_pov = 3

for i in range(count_pov):
    range_num = ''.join(range_num.split(hidden_number[i]))
    hidden_number += choice(range_num)
n = 0
while n < 6:
    num = input("Введи четырёхзначное число: ")
    unique = set(num)
    if len(num) != 4:
        print("И что ты ввел?")
        continue
    if len(set(hidden_number)) != len(unique):
        print('Цифры не должны повторяться')
        continue
    if num.islower():
        print('На буквах играться со мной нельзя!')
        continue
    n += 1
    bull = 0
    cow = 0
    for i in range(4):
        if hidden_number[i] == num[i]:
            bull += 1
        elif num[i] in hidden_number:
            cow += 1
    print(num + ' содержит ' + str(bull) + ' быка и ' + str(cow) + ' коровы')
    if bull == 4:
        print('Вы выиграли!')
        break
