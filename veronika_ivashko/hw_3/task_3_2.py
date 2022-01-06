"""
2. Напишите программу, которая добавляет ‘ing’ к словам
"""

some_words = 'test some more'
postfix = 'ing'
result = ' '.join([word + postfix for word in some_words.split()])

print(f'If we add ({postfix}) to ({some_words}), \
the result will be ({result}).')
