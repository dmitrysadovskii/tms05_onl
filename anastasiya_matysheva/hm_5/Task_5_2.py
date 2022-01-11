def eng(my_string):
    if len(my_string) > 3:
        print("{}, {} and {} like this".format(my_string[0], my_string[1], len(my_string) - 2))
    elif len(my_string) == 3:
        print("{}, {} and {} like this".format(my_string[0], my_string[1], my_string[2]))
    elif len(my_string) == 2:
        print("{} and {} like this".format(my_string[0], my_string[1]))
    elif len(my_string) == 1:
        print("{} like this".format(my_string[0]))
    else:
        print("no one likes this")


def rus(my_string):
    if len(my_string) > 3:
        print("{}, {} и {} нравится запись".format(my_string[0], my_string[1], len(my_string) - 2))
    elif len(my_string) == 3:
        print("{}, {} и {} нравится запись".format(my_string[0], my_string[1], my_string[2]))
    elif len(my_string) == 2:
        print("{} и {} нравится запись".format(my_string[0], my_string[1]))
    elif len(my_string) == 1:
        print("{} нравится запись".format(my_string[0]))
    else:
        print("no one likes this")


def choose_lang(my_string):
    count = False
    if len(my_string) <= 0:
        print("no one likes this")
    else:
        for i in my_string[0]:
            if ord(i) > 127:
                count = True
        if count:
            rus(my_string)
        else:
            eng(my_string)


if __name__ == '__main__':
    my_string = input("Enter name: ")
    l = my_string.split()
    choose_lang(l)
