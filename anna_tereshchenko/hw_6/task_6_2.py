def count(input_string):
    items = list(input_string)
    res = ''
    for i, v in enumerate(items):
        flag = True
        c = 1
        while flag:
            if i < len(items) - 1 and v == items[i + 1]:
                items.pop(i + 1)
                c += 1
            else:
                flag = False
                iterations = c if c != 1 else ''
                res += f'{v}{iterations}'
    return res


print(count('abcdddeeeaaa'))
