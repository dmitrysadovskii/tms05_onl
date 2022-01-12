def count_str(stroka):
    param = list(stroka)
    itog = ''
    for k, v in enumerate(param):
        data = True
        n = 1
        while data:
            if k < len(param) - 1 and v == param[k + 1]:
                param.pop(k + 1)
                n += 1
            else:
                data = False
                iterations = n if n != 1 else ''
                itog += f'{v}{iterations}'
    print(itog)


count_str('aaabbdefffff')
count_str('aaaaaaabbbbbbfhdjuuuuu')
