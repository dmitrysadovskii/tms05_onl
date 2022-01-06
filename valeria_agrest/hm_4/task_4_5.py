dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'd': 4, 'e': 5}
dict3 = {}

for key in dict1.keys():
    if key in dict2:
        dict3[key] = [dict1[key], dict2[key]]
    else:
        dict3[key] = [dict1[key], 'None']

for key in dict2.keys():
    if key in dict1:
        dict3[key] = [dict2[key], dict1[key]]
    else:
        dict3[key] = ['None', dict2[key]]

print(dict3)
