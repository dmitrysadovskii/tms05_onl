alphabetEN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphabetRU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
offset = int(input('Step: '))
message = input("Message: ").upper()
result = ''
lang = input('Enter language RU/EU: ')
if lang == 'RU':
    for i in message:
        place = alphabetRU.find(i)
        new_place = place + offset
        if i in alphabetRU:
            result += alphabetRU[new_place]
        else:
            result += i
else:
    for i in message:
        place = alphabetEN.find(i)
        new_place = place + offset
        if i in alphabetEN:
            result += alphabetEN[new_place]
        else:
            result += i

print(result)
