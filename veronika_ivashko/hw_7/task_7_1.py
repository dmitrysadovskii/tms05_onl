"""
1. Напишите функцию, которая принимает на вход одномерный массив и два числа -
размеры выходной матрицы. На выход программа должна подавать матрицу нужного
размера, сконструированную из элементов массива.
reshape([1, 2, 3, 4, 5, 6], 2, 3) =>
[
    [1, 2, 3],
    [4, 5, 6]
]
reshape([1, 2, 3, 4, 5, 6, 7, 8,], 4, 2) =>
[
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]
"""


def reshape(some_numbers: list, num_rows: int, num_cols: int) -> list:
    """
    Return two-dimensional matrix from input numbers due to number of rows and
    columns specified in function. If number of elements is greater than
    necessary number of elements, input list will be truncated. If number of
    elements is less than the necessary, the rest numbers will be zeros.
    Number of rows and columns specify number of necessary elements.
    :param some_numbers: list of numbers to transform.
    :param num_rows: number of rows in result matrix.
    :param num_cols: number of columns in result matrix.
    :return: matrix with input numbers of specified rows and columns.
    """
    numbers_length = len(some_numbers)
    actual_length = num_cols * num_rows
    if actual_length > numbers_length:
        some_numbers.extend([0 for _ in range(actual_length - numbers_length)])

    prev_i = 0
    result_matrix = []
    for i in range(num_cols, actual_length+1, num_cols):
        result_matrix.append(some_numbers[prev_i:i])
        prev_i = i
    return result_matrix


print(reshape([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3], 3, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3], 3, 4))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3], 4, 2))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3], 4, 5))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3], 3, 5))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))
print(reshape([], 4, 2))
