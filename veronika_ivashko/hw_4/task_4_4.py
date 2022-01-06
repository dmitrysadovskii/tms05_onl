from random import randint

"""
4. Создайте список из 10 элементов, 
вставьте на 3-ю позицию новое значение, 
удалите элемент из списка под индексом 6
"""

num_list = [randint(0, 100) for i in range(10)]
print(f'Original list is: {num_list}')

num_list.insert(3, randint(101, 1000))
print(f'List with inserted element: {num_list}')

num_list.pop(6)
print(f'List without sixth element: {num_list}')
