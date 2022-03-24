"""Task number 1:
Напишите генератор который принимает список numbers
= [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
и возвращает новый список только с положительными числами
"""


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
numbers_positive = [x if x > 0 else -x for x in numbers]
print(numbers_positive)

"""Task number 2:
Необходимо составить список чисел которые указывают на длину слов в строке:
sentence = " thequick brown fox jumps over the lazy dog",
но только если слово не "the".
"""

just_string = ' thequick brown fox jumps over the lazy dog'.split()
words_length = [len(i) for i in just_string if i != 'the']
print(words_length)
