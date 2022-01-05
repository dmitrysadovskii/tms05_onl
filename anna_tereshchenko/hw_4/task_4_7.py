from collections import Counter

str1 = 'HhHeAaao $%^&((((({:'
str1 = str1.lower()
arr = list(filter(str.islower, str1))
arr.sort()
c = Counter(arr)
a = c.most_common(1)
(c, d) = (a[0])
print(c)
