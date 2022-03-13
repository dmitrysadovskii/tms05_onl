# Генераторы

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numbers = [x for x in numbers if x > 0]
print(positive_numbers)

sentence = "the quick brown fox jumps over the lazy dog"
new_sentence = [len(i) for i in sentence.split() if i != 'the']
print(new_sentence)
