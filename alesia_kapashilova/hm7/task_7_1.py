def reshape(first_array: list, num_rows: int, num_col: int) -> list:
    num_len = len(first_array)
    actual_len = num_col * num_rows
    if actual_len > num_len:
        print('Длина списка не соответствует введенным значениям!!!')
        return []
    new_array = []
    for i in range(num_rows):
        new_array.append([first_array[k] for k in
                          range(num_col * i, num_col * i + num_col)])

    if actual_len != len(first_array):
        new_array.append(first_array[actual_len:])

    return new_array


print(reshape([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8, ], 4, 2))
