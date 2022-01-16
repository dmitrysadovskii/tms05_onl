def encode_decode(str1: str, num: int, option: str):
    """""
    Основное задание + 3 пункта в бонусных очках
    """""
    alphabet_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                  'abcdefghijklmnopqrstuvwxyz'
    alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРС' \
                  'ТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''
    if option == 'encode':
        for i in str1:
            if i in alphabet_en:
                position = alphabet_en.find(i)
                new_position = position + num
                result += alphabet_en[new_position]
            elif i in alphabet_ru:
                position = alphabet_ru.find(i)
                new_position = position + num
                result += alphabet_ru[new_position]
            else:
                result += i
        print(result)
    if option == 'decode':
        for i in str1:
            if i in alphabet_en:
                position = alphabet_en.find(i)
                new_position = position - num
                result += alphabet_en[new_position]
            elif i in alphabet_ru:
                position = alphabet_ru.find(i)
                new_position = position - num
                result += alphabet_ru[new_position]
            else:
                result += i
        print(result)


encode_decode('hello world!', 3, 'encode')
encode_decode('ymnx Nx f yjXy xyWnsl', 5, 'decode')
