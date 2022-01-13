string = input("Write string : ")

count = {}
for s in string:
    if s in count:
        count[s] += 1
    else:
        count[s] = 1

result_string = ""

for key in count:
    if count[key] == 1:
        result_string += key
    elif count[key] > 1:
        result_string += key
        result_string += str(count[key])

print(result_string)
