# В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
str = 'Ivanou Ivan'
new_str = ' '.join(str.split(' ')[::-1])
print(new_str)
