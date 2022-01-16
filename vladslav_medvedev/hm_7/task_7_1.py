'''
1. Напишите функцию, которая принимает на вход одномерный массив и два числа
- размеры выходной матрицы. На выход программа должна подавать матрицу
нужного размера, сконструированную из элементов массива.
reshape([1, 2, 3, 4, 5, 6], 2, 3) =>
[
    [1, 2, 3],
    [4, 5, 6]
]
reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2) =>
[
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]
'''
def reshape(array_1: list, row, column) -> list:
    matrix_size = row * column
    if matrix_size > len(array_1):
        print('Matrix size does not match the number of array elements')
        return
    prev_i = 0
    matrix_result = []
    for i in range(column, matrix_size + 1, column):
        matrix_result.append(array_1[prev_i:i])
        prev_i = i
    return matrix_result

print(reshape([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))
