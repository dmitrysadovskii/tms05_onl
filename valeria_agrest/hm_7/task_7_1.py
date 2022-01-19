# 1
def reshape(list_1: list, num_1: int, num_2: int) -> list:
    array = []
    for i in range(num_1):
        while len(list_1) > num_2:
            part = list_1[:num_2]
            array.append(part)
            list_1 = list_1[num_2:]
        array.append(list_1)
        return array


print(reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))


# 1 генераторы
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
number_plus = [x for x in numbers if x >= 0]
print(number_plus)


# 2 генераторы
sentence = 'thequick brown fox jumps over the lazy dog'
length_of_words = [len(x) for x in sentence.split() if x != ' the ']
print(length_of_words)
