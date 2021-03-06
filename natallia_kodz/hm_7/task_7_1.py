def reshape(initial_list, rows_num, elements_num):
    result_list = []
    assert len(initial_list) == rows_num * elements_num, \
        "Initial number of elements can't be transformed into requested matrix"
    for i in range(rows_num):
        result_list.append([initial_list[x] for x in
                            range(elements_num * i,
                                  (elements_num * i + elements_num))])
    return result_list


print(reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))
