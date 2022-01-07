from random import choice

z = '0123456789'
x = choice(z[1:10])
for i in range(3):
    z = ''.join(z.split(x[i]))
    x += choice(z)
n = 0
while True:
    y = input("Введите четырёхзначное число: ")
    n += 1
    bull = 0
    cow = 0
    for i in range(4):
        if x[i] == y[i]:
            bull += 1
        elif y[i] in x:
            cow += 1
    print(y + ' содержит ' + str(bull) + ' быка и ' + str(cow) + ' коровы')
    if bull == 4:
        print('Вы выиграли!')
        break
