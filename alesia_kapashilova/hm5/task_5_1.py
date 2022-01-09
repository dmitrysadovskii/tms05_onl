from random import choice

range_num = '0123456789'
hidden_number = choice(range_num[0:10])
count_pov = 3
for i in range(count_pov):
    range_num = ''.join(range_num.split(hidden_number[i]))
    hidden_number += choice(range_num)
n = 0
while n < 6:
    my_num = input("Введи четырёхзначное число: ")
    if len(my_num) != 4:
        print("И что ты ввел?")
        continue
    n += 1
    bull = 0
    cow = 0
    for i in range(4):
        if hidden_number[i] == my_num[i]:
            bull += 1
        elif my_num[i] in hidden_number:
            cow += 1
    print(
        my_num + ' содержит ' + str(bull) + ' быка и ' + str(cow) + ' коровы')
    if bull == 4:
        print('Вы выиграли!')
        break
