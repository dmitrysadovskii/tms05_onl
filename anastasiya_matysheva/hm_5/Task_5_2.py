def eng(like_list):
    if len(like_list) > 3:
        print("{}, {} and {} like this".format(like_list[0],
                                               like_list[1],
                                               len(like_list) - 2))
    elif len(like_list) == 3:
        print("{}, {} and {} like this".format(like_list[0],
                                               like_list[1],
                                               like_list[2]))
    elif len(like_list) == 2:
        print("{} and {} like this".format(like_list[0], like_list[1]))
    elif len(like_list) == 1:
        print("{} like this".format(like_list[0]))
    else:
        print("no one likes this")


def rus(like_list):
    if len(like_list) > 3:
        print("{}, {} и {} нравится запись".format(like_list[0],
                                                   like_list[1],
                                                   len(like_list) - 2))
    elif len(like_list) == 3:
        print("{}, {} и {} нравится запись".format(like_list[0],
                                                   like_list[1],
                                                   like_list[2]))
    elif len(like_list) == 2:
        print("{} и {} нравится запись".format(like_list[0], like_list[1]))
    elif len(like_list) == 1:
        print("{} нравится запись".format(like_list[0]))
    else:
        print("Не нравится ни одна запись")


def choose_lang(like_list):
    lang = 'en'
    if len(like_list) <= 0:
        print("no one likes this")
    else:
        for i in like_list[0]:
            if ord(i) > 127:
                lang = 'ru'
        if lang == 'ru':
            rus(like_list)
        else:
            eng(like_list)


if __name__ == '__main__':
    like_list = input("Enter name: ")
    like = like_list.split()
    choose_lang(like)