sentence = "I learn Python"
words = sentence.split()
words1 = [word + 'ing' for word in words]
sentence1 = (" ".join(words1))
print(sentence1)
