"""
3. В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
"""

some_string = 'Ivanou Ivan'
some_string_splited = some_string.split()[::-1]
result = ' '.join(some_string_splited)

print(f'String "{some_string}" is transformed into "{result}".')
