def logic(i, num, option, alphabet):
    position = alphabet.find(i)
    new_position = 0
    if option == "encode":
        new_position = position + num
    elif option == "decode":
        new_position = position - num
    return alphabet[new_position]


def encode_decode(str1: str, num: int, option: str):
    """""
    Основное задание + 3 пункта в бонусных очках
    """""
    alphabet_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                  'abcdefghijklmnopqrstuvwxyz'
    alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРС' \
                  'ТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''
    for i in str1:
        if i in alphabet_ru:
            result += logic(i, num, option, alphabet_ru)
        elif i in alphabet_en:
            result += logic(i, num, option, alphabet_en)
        else:
            result += i
    return result


print(encode_decode('hello world!', 3, 'encode'))
print(encode_decode('ymnx Nx f yjXy xyWnsl', 5, 'decode'))
