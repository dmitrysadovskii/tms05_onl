"""Function that takes list, quantity of rows and columns"""


def reshape_list(array_num_one: list, rows: int, columns: int):
    """Counting the length of array"""
    num_len = len(array_num_one)
    """Colums and rows multiplications"""
    columns_x_rows = columns * rows
    """If condition comparing array length and multiplication result"""
    if columns_x_rows > num_len:
        array_num_one.extend([0 for _ in range(columns_x_rows - num_len)])
    j = 0
    new_array = []
    """Using append method to create new array in
    range containing colums quantity and multiplication result
    """
    for i in range(columns, columns_x_rows + 1, columns):
        new_array.append(array_num_one[j:i])
        j = i
    return new_array


print(reshape_list([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape_list([1, 2, 3, 4, 5, 6, 7, 8, ], 4, 2))
