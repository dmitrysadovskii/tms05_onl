def reshape(arr, string_numb, column_numb):
    size_m = column_numb * string_numb
    if size_m > len(arr):
        print('Matrix size does not match the number of array elements')
        return

    n = 0
    matrix = []
    for i in range(column_numb, size_m + 1, column_numb):
        matrix.append(arr[n:i])
        n = i
    return matrix


print(reshape([1, 2, 3, 4, 5, 6], 2, 3))
print(reshape([1, 2, 3, 4, 5, 6, 7, 8, ], 4, 2))
