"""
4. Напишите программу которая удаляет пробел в начале, в конце строки
"""

some_string = '    test some more case         '
result = some_string.strip()

print(f'Length of initial row "{some_string}" is {len(some_string)} symbols.')
print(f'Length of cleansed row "{result}" is {len(result)} symbols.')
