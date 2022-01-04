"""Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
удалите элемент из списка под индексом 6
"""
list = ['Merry', 'christmas', 'and', 'week', 'new',
        '20', '22', 'year', 'TMS', 'Qa_pyton']
list.insert(3, "happy")
del list[6]
print(list)
