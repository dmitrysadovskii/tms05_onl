p = input('Ivanov Ivan')
name = p[:p.find('Ivan')]
surname = p[p.find('Ivanov') + 1:]
print(surname + ' ' + name)
