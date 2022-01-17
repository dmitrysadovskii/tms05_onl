eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
symbol = [" ", ",", ".", "!", "?"]

print("Выберите язык: aнгл=e, рус=r")
lan = input()
print("Выберите шифрование: шифрование - ch, дешифрование - def")
chif = input()
print("Введите ключ шифрования")
key = int(input())
print("Введите фразу")
phrase = input()


def chru(chifr, k, lang, fraza):
    if lang == 'r':
        moch = 32
    if lang == 'e':
        moch = 26
    if chifr == 'def':
        k = -k
    for i in range(len(fraza)):
        if fraza[i].isalpha():
            if fraza[i] == fraza[i].upper():
                for j in range(moch):
                    if moch == 32:
                        if fraza[i] == rus_upper_alphabet[j]:
                            print(rus_upper_alphabet[(j + k) % moch], end='')
                            break
                    if moch == 26:
                        if fraza[i] == eng_upper_alphabet[j]:
                            print(eng_upper_alphabet[(j + k) % moch], end='')
                            break
            elif fraza[i] == fraza[i].lower():
                for j in range(moch):
                    if moch == 32:
                        if fraza[i] == rus_lower_alphabet[j]:
                            print(rus_lower_alphabet[(j + k) % moch], end='')
                            break
                    if moch == 26:
                        if fraza[i] == eng_lower_alphabet[j]:
                            print(eng_lower_alphabet[(j + k) % moch], end='')
                            break
        else:
            print(fraza[i], end='')


chru(chif, key, lan, phrase)
