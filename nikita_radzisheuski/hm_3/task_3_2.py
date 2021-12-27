
"""Adding ing to words. In my case I created string with text ->
splitted words -> added ing -> transformed it back to str"""

string_with_words = 'This is string for homework number three and to add ing'
splitting_the_words = string_with_words.split()
splitting_the_words = [words + "ing" for words in splitting_the_words]
list_to_string = ' '.join([str(elem) for elem in splitting_the_words])

print(list_to_string)
