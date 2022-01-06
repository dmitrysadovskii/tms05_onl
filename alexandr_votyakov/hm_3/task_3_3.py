s = "Ivanou Ivan"
spc = (s.find(" "))
surname = s[:spc]
name = s[spc + 1:]
print(name, surname)
