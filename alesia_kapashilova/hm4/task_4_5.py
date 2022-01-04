a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
q = {q: [a.get(q, None), b.get(q, None)] for q in sorted(set(a) | set(b))}
print(q)
