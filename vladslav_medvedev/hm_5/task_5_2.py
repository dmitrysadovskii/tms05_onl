'''
Like
likes() -> "no one likes this"
likes("Ann") -> "Ann likes this"
likes("Ann", "Alex") -> "Ann and Alex like this"
likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this"
likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this"
'''


def eng():
    array = choices
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
    array = choices
    array = array.split()
    count = len(array)
    if count == 0:
        print("Никому не понравилось")
    elif count < 2:
        print(f"Пользователю {array[0]} это понравилось")
    elif count < 3:
        print(f"Пользователям {array[0]} и {array[1]} это понравилось")
    elif count < 4:
        print(f"Пользователям {array[0]}, {array[1]}"
              f" и {array[2]} это понравилось")
    elif count >= 4:
        count = count - 2
        print(f"Пользователям {array[0]}, {array[1]} и"
              f" {count} другим это понравилось")

list_eng = 'a, b, c, d, e, f, g, h,i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
choices = input("Write list of people: / Введите имена людей: ")
for i in choices:
    if i.lower() in list_eng:
        choice = 1
        eng()
        break
    else:
        choice = 2
        rus()
        break
