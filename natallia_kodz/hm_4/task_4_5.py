a = {"a": 1, "b": 2, "c": 3}
b = {"c": 3, "d": 4, "e": 5}
new_a = a.copy()
new_a.update(b)
both_keys = list(new_a)
ab = {}
for k in both_keys:
    if k in a and k in b:
        ab[k] = [a[k], b[k]]
    elif k in a:
        ab[k] = [a[k], None]
    else:
        ab[k] = [None, b[k]]
print(ab)
