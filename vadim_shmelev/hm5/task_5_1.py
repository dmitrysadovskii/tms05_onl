from random import choice
a = '1234567890'
x = choice(a)
for i in range(3):
    x = x + choice(a)

print('#spoiler# answer:' + x)

while True:
    y = input('enter 4-digit number:')
    b = 0
    c = 0
    for i in range(4):
        if x[i] == y[i]:
            b = b+1
        elif y[i] in x:
            c = c+1
    print(y + ' is ' + str(b) + ' bulls and ' + str(c) + ' cows')
    if b == 4:
        print('You win!!!!!')
        break
