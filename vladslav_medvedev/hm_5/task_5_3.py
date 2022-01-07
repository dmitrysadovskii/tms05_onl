'''
BuzzFuzz
'''
for i in range(0, 100):
    if i % 3 == 0 and i % 5 == 0:
        print('BuzzFuzz')
    elif i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
