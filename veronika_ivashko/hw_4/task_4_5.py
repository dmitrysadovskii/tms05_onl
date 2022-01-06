from collections import defaultdict

"""
5. Есть 2 словаря
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': 5}

Необходимо их объединить по ключам, а значения ключей поместить в список, 
если у одного словаря есть ключ "а", а у другого нету, 
то поставить значение None на соответствующую позицию
(1-я позиция для 1-ого словаря, вторая для 2-ого)
ab = {
    'a': [1, None], 
    'b': [2, None], 
    'c': [3, 3], 
    'd': [None, 4], 
    'e': [None, 5]
}
"""

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
c = {'f': 3, 'z': 4, 'a': 5}


def merge_multiple_dicts(*args: dict) -> defaultdict:
    result_dict = defaultdict(list)
    all_keys = []
    for el in args:
        all_keys.extend([item for item in list(el.keys())
                         if item not in all_keys])
    for key in all_keys:
        for el in args:
            result_dict[key].append(el.get(key))
    return result_dict


print(merge_multiple_dicts(a, b, c))
print(merge_multiple_dicts(a, b))
