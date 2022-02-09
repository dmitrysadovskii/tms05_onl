def number_of_letters(word):
    array = {}
    str1 = ''
    for el in word:
        array[el] = word.count(el)
    for k in array.keys():
        if array[k] == 1:
            str1 += k
        else:
            str1 += k + str(array[k])
    print(str1)


number_of_letters('aaabbbcccdddeeele')
