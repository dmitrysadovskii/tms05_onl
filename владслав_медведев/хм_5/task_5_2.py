'''
Like
likes() -> "no one likes this"
likes("Ann") -> "Ann likes this"
likes("Ann", "Alex") -> "Ann and Alex like this"
likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this"
likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this"
'''


def eng()
def eng(choices):
    choices = choices.split()
    count = len(choices)
    if count == 0:
        print("No one likes this")
    elif count < 2:
        print(f"{choices[0]} likes this")
    elif count < 3:
        print(f"{choices[0]} and {choices[1]} like this")
    elif count < 4:
        print(f"{choices[0]}, {choices[1]} and {choices[2]} like this")
    elif count >= 4:
        count = count - 2
        print(f"{choices[0]}, {choices[1]} and {count} other like this")


def rus(choices):
    choices = choices.split()
    count = len(choices)
    if count == 0:
        print("Никому не понравилось")
    elif count < 2:
        print(f"Пользователю {choices[0]} это понравилось")
    elif count < 3:
        print(f"Пользователям {choices[0]} и {choices[1]} это понравилось")
    elif count < 4:
        print(f"Пользователям {choices[0]}, {choices[1]}"
              f" и {choices[2]} это понравилось")
    elif count >= 4:
        count = count - 2
        print(f"Пользователям {choices[0]}, {choices[1]} и"
              f" {count} другим это понравилось")


list_eng = 'a, b, c, d, e, f, g, h,i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z'
choices = input("Введите имена людей:/ Write list of people: ")
for i in choices:
    if i.lower() in list_eng:
        choice = 1
        eng(choices)
        break
    else:
        choice = 2
        rus(choices)
        break

