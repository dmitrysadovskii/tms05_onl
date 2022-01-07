"""
*1) Вам передан массив чисел. Известно, что каждое число в этом массиве
имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
Напишите программу, которая будет выводить уникальное число
"""


def get_unique_values(non_unique_values: list) -> list:
    return [item for item in non_unique_values
            if non_unique_values.count(item) == 1]


print(get_unique_values([1, 5, 2, 9, 2, 9, 1]))
