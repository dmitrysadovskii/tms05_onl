all_numb = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_numb = [x if x > 0 else -x for x in all_numb]
positive_numb = str(positive_numb)

sentence = "the quick brown fox jumps over the lazy dog"
new_sentence = [len(y) for y in sentence.split() if y != 'the']

print(f'positive numbers from the list: {positive_numb}')

print(f'the length of the words in the string except "the": {new_sentence}')
