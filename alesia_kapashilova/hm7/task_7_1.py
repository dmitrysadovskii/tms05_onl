def reshape(first_array: list, num_rows: int, num_col: int) -> list:
    num_len = len(first_array)
    actual_len = num_col * num_rows
    if actual_len > num_len:
        first_array.extend([0 for _ in range(actual_len - num_len)])

    k = 0
    new_array = []
    for i in range(num_col, actual_len + 1, num_col):
        new_array.append(first_array[k:i])
        k = i
    return new_array


print(reshape([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8, ], 4, 2))
