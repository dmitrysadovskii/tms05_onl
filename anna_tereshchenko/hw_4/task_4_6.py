a = [1, 5, 2, 9, 2, 9, 1]
a.sort()
i = 0
for k in range(len(a)):
    if (i < len(a) - 1) and (a[i] != a[i + 1]):
        print(a[i])
    i += 2
