a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4,'e': 5}
update = {update: [a.get(update, None), b.get(update, None)] for update in sorted(set(a) | set(b))}
print(update)
