'''
Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ
заменяется другим, отстоящим от него в алфавите на фиксированное число позиций
Примеры:
hello world! -> khoor zruog!
this is a test string -> ymnx nx f yjxy xywnsl

Напишите две функции - encode и decode принимающие как
параметр строку и число - сдвиг.
'''


def codding_func(alphabet, cypher_result,cypher):
    alphabet = alphabet * 3
    #Строку увеличил для того чтобы если индекс введенного
    #значения будет больше длинны алфавита!
    for i in cypher:
        if i == ' ' or i == cypher.isalpha():
            cypher_result += i
        elif i in signs:
            cypher_result += i
        else:
            number_in_str = alphabet.find(i)
            number_in_next_str = number_in_str + 3
            cypher_result = cypher_result + alphabet[number_in_next_str]
    return cypher_result


def uncodding_func(alphabet,cypher_result,uncypher):
    alphabet = alphabet * 3
    for i in uncypher:
        if i == ' ' or i == uncypher.isalpha():
            cypher_result += i
        elif i in signs:
            cypher_result += i
        else:
            number_in_str = alphabet.find(i)
            number_in_next_str = number_in_str - 5
            cypher_result = cypher_result + alphabet[number_in_next_str]
    return cypher_result


alphabet = 'abcdefghijklmnopqrstuvwxyz'
signs = ",.;:!?)(\/"
cypher = 'hello world!'
uncypher = 'ymnx nx f yjxy xywnsl'
cypher_result = ''
print(codding_func(alphabet, cypher_result,cypher))
print(uncodding_func(alphabet, cypher_result,uncypher))
