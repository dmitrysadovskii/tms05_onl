from collections import Counter

"""
*2) Дан текст, который содержит различные английские буквы и знаки препинания.
Вам необходимо найти самую частую букву в тексте.
Результатом должна быть буква в нижнем регистре.
При поиске самой частой буквы, регистр не имеет значения,
так что при подсчете считайте, что "A" == "a". Убедитесь, что вы не считайте
знаки препинания, цифры и пробелы, а только буквы.
Если в тексте две и больше буквы с одинаковой частотой,
тогда результатом будет буква, которая идет первой в алфавите.
Для примера, "one" содержит "o", "n", "e" по одному разу,
так что мы выбираем "e".

"a-z" == "a"
"Hello World!" == "l"
"How do you do?" == "o"
"One" == "e"
"Oops!" == "o"
"AAaooo!!!!" == "a"
"a" * 9000 + "b" * 1000 == "a"
"""

lorem_ipsum = '''Lorem ipsum.,- dolor sit amet, consectetur adipiscing elit,
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco '''


def count_most_common_letter(some_text: str) -> str:
    splited_text = some_text.split()
    symbols = [symbol for element in splited_text
               for symbol in list(element.lower())]
    cleansed_symbols = [el for el in symbols if 97 <= ord(el) <= 122]
    max_cnt = 0
    most_common_symbol = None
    for k, v in Counter(sorted(cleansed_symbols)).items():
        if v > max_cnt:
            most_common_symbol, max_cnt = k, v
    return most_common_symbol


print(count_most_common_letter(lorem_ipsum))
print(count_most_common_letter('a-z'))
print(count_most_common_letter('Hello World!'))
print(count_most_common_letter('How do you do?'))
print(count_most_common_letter('One'))
print(count_most_common_letter('Oops!'))
print(count_most_common_letter('AAaooo!!!!'))
print(count_most_common_letter("a" * 9000 + "b" * 1000))
