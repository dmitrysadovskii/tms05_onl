def reshape(array: list, rows: int, amount: int) -> list:
    numb_len = len(array)
    list_len = amount * rows

    if list_len > numb_len:
        array.extend([0 for _ in range(list_len - numb_len)])

    k = 0
    actual_array = []
    for i in range(amount, list_len + 1, amount):
        actual_array.append(array[k:i])
        k = i
    return actual_array


print(reshape([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8, ], 4, 2))
