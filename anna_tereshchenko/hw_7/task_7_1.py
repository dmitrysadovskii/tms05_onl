def reshape(arr1: list, elem_string: int, elem_count: int) -> list:
    m_size = elem_string * elem_count
    if m_size > len(arr1):
        print('Размер матрицы не соответсвует количеству '
              'переданных элементов в массиве')
        return []
    arr2 = []
    for i in range(elem_string):
        arr2.append([arr1[k] for k in range(elem_count * i,
                    (elem_count * i + elem_count))])

    if m_size != len(arr1):
        arr2.append(arr1[m_size:])

    return arr2


print(reshape([1, 2, 3, 4, 5, 6], 2, 3))


numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
numbers = [i for i in numbers if i > 0]
print(numbers)
sentence = " the quick brown fox jumps over the lazy dog"
arr = [len(i) for i in sentence.split() if i != 'the']
print(arr)
