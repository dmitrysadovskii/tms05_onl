# 1
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numb = [n for n in numbers if n > 0]
print(positive_numb)

# 2
sentence = "the quick brown fox jumps over the lazy dog"
list_numb = [len(s) for s in sentence.split() if s != 'the']
print(list_numb)
