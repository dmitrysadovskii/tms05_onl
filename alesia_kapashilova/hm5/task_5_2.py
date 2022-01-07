def eng():
    array = input('Write list of people: ')
    array = array.split()
    count = len(array)
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
    array = input('Введите имена людей: ')
    array = array.split()
    count = len(array)
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
        print(f"{array[0]}, {array[1]} и {count} другим это понравилось")


mydict = {1: eng, 2: rus}
choices = list(map(int, input("Do you want to: \n(1)Eng \n(2)Rus\n").split()))
for choice in choices:
    if 0 < choice and choice < 3:
        mydict[choice]()
    else:
        print("That is not between 1 and 2! Try again:")
