n = [1, 5, 2, 9, 2, 9, 1]
print(list(set(i for i in n if n.count(i) == 1)))
