array = input('Write list of people: ')
array = array.split()
count = len(array)

def eng():
    global count
    if count == 0:
        print("No one likes this")
    elif count < 2:
        print(f"{array[0]} likes this")
    elif count < 3:
        print(f"{array[0]} and {array[1]} like this")
    elif count < 4:
        print(f"{array[0]}, {array[1]} and {array[2]} like this")
    elif count >= 4:
        count = count - 2
        print(f"{array[0]}, {array[1]} and {count} other like this")


def rus():
    global count
    if count == 0:
        print("Никому не понравилось")
    elif count < 2:
        print(f"{array[0]} это понравилось")
    elif count < 3:
        print(f"{array[0]} и {array[1]} это понравилось")
    elif count < 4:
        print(f"{array[0]}, {array[1]} и {array[2]} это понравилось")
    elif count >= 4:
        count = count - 2
        print(
            f"{array[0]}, {array[1]} и {count} другим это понравилось")


if len(array) > 0 and (65 <= ord(array[0][0].lower()) <= 122):
    eng()
elif len(array) > 0 and (1040 <= ord(array[0][0].lower()) <= 1103):
    rus()
