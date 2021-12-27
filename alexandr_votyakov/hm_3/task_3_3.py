s = "Ivanou Ivan"
spc = (s.find(" "))
surname = s[:spc]
print(surname)
name = s[spc+1:]
print(name)
print(name, surname)
