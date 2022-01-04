from collections import Counter

a = '"a" * 9000 + "b" * 1000'
dictionary = {}
for key1, value in Counter(a).items():
    if key1.isalpha():
        dictionary[key1] = value

print(sorted(dictionary.items(), key=lambda x: x[1], reverse=True)[0][0])
