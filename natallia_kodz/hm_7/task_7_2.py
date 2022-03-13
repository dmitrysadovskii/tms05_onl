# 1.1
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
new_list = [abs(x) for x in numbers]
print(new_list)

# 1.2
numbers2 = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
new_list2 = [y for y in numbers2 if y > 0]
print(new_list2)

# 2
sentence = " thequick brown fox jumps over the lazy dog"
sentence_list = sentence.split()
print(sentence_list)
number_list = [len(z) for z in sentence_list if z != "the"]
print(number_list)
