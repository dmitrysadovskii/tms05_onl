import string

EN_ALPHABET = string.ascii_lowercase
RU_ALPHABET = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
DECODE = 'de'
ENCODE = 'en'
RU = 'ru'
EN = 'en'


def language_detection(str1: str):
    language = EN
    for i in str1:
        for j in i:
            if ord(j) in range(1040, 1104):
                language = RU
            break
        break
    return language


def format_case(to_compare: str, to_return: str):
    return to_return.lower() \
        if to_compare.islower() else to_return.upper()


def caesar_code(str1: str, shift: int, operation):
    shift = (-shift) if operation == DECODE else shift
    alphabet = RU_ALPHABET if language_detection(str1) == RU else EN_ALPHABET
    str2 = ''
    for k in str1:
        tmp = k.lower()
        al_k_index = alphabet.find(tmp)
        if tmp not in alphabet:
            str2 = str2 + k
        elif (al_k_index + shift + 1) > len(alphabet):
            new_index = al_k_index + shift - len(alphabet)
            while (new_index + 1) > len(alphabet):
                new_index = new_index - len(alphabet)
            k = format_case(k, alphabet[new_index])
            str2 = str2 + k
        else:
            k = format_case(k, alphabet[al_k_index + shift])
            str2 = str2 + k

    print(str2)


caesar_code('Hello World!', 3, ENCODE)
caesar_code('Khoor Zruog!', 3, DECODE)


def a1z26_code(str1: str):
    """""
    БОНУСНЫЙ ОЧКИ
    4. Придумайте свой шифр
    Шифр A1Z26
    Это простая подстановка, где каждая буква заменена 
    её порядковым номером в алфавите.
    Программа работает только с русским языком
    (было лень добавлять поддержку языков, сделала это в шифре Цезаря)
    """""

    new_str = ''
    i = 0
    for k in str1:
        k = k.lower()
        if k not in RU_ALPHABET:
            new_str = new_str + k
        elif (i < len(str1) - 1) and str1[i].lower() in RU_ALPHABET \
                and str1[i + 1].lower() not in RU_ALPHABET:
            new_str = f'{new_str}{str(RU_ALPHABET.find(k) + 1)}'
        elif (i + 1) < len(str1):
            new_str = f'{new_str}{str(RU_ALPHABET.find(k) + 1)}-'
        else:
            new_str = f'{new_str}{str(RU_ALPHABET.find(k) + 1)}'
        i += 1

    print(new_str)


a1z26_code('ПрИвеТ, МиР!')
