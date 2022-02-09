a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
ab = {k: [a.get(k), b.get(k)] for k in a.keys() | b.keys()}
print(ab)
