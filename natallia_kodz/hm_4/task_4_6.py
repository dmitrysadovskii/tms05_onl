a = [1, 5, 2, 9, 2, 9, 1]
unique = []
for i in a:
    if a.count(i) == 1:
        unique.append(i)
print(unique)
