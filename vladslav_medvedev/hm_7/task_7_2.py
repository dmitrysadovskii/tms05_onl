'''
1.Напишите генератор который принимает список
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
и возвращает новый список только с положительными числами
'''
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
def gen_numbers(numbers):
    n = 0
    for i in numbers:
        if numbers[n] > 0:
            n += 1
        elif numbers[n] < 0:
            a = abs(float(numbers[n]))
            numbers.remove(i)
            numbers.insert(n, a)
            n += 1
    return numbers

print(gen_numbers(numbers))

'''
Необходимо составить список чисел которые указывают на длину слов в строке:
sentence = " thequick brown fox jumps over the lazy dog",
но только если слово не "the".
Для проверки было вставлено еще одно 'the'
'''
sentence = 'thequick brown the fox jumps over the lazy dog'


def sentences():
    arr = [len(i) for i in sentence.split() if i != 'the']
    return arr

print(sentences())

