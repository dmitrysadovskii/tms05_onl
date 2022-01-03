a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
c = {d: [a.get(d, None), b.get(d, None)] for d in sorted(set(a) | set(b))}
print(c)
