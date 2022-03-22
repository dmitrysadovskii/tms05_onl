chars = "abcdefghijklmnopqrstuvwxyz"
check_string = input("write something: ")
chars_new = ""
for char in chars:
    count = check_string.count(char)
    if count > 1:
        countstr = str(count)
        chars_new = chars_new + char + countstr
    if count == 1:
        chars_new = chars_new + char
print(chars_new)
