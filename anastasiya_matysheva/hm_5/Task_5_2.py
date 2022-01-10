def eng(name):
    if len(like_list) > 3:
        return '{}, {} and {} like this'.format(like_list[0], like_list[1], len(like_list) - 2)
    elif len(like_list) == 3:
        return '{}, {} and {} like this'.format(like_list[0], like_list[1], like_list[2])
    elif len(like_list) == 2:
        return '{} and {} like this'.format(like_list[0], like_list[1])
    elif len(like_list) == 1:
        return '{} like this'.format(like_list[0])
    else:
        return 'no one likes this'


def rus(name):
    if len(like_list) > 3:
        return '{}, {} и {} нравится эта запись'.format(like_list[0], like_list[1], len(like_list) - 2)
    elif len(like_list) == 3:
        return '{}, {} и {} нравится эта запись'.ormat(like_list[0], like_list[1], like_list[2])
    elif len(like_list) == 2:
        return '{} и {} нравится эта запись'.format(like_list[0], like_list[1])
    elif len(like_list) == 1:
        return '{} нравится эта запись'.format(like_list[0])
    elif len(like_list) <= 0:
        return 'Никому не нравится эта запись'


def choose_lang(name):
    count = False
    if len(like_list) <= 0:
        print('no one likes this')
    else:
        for i in like_list[0]:
            if ord(i) > 127:
                count = True
        if count:
            rus(name)
        else:
            eng(name)


if __name__ == '__main__':
    like_list = input('Enter username: ')
    like = like_list.split()
    choose_lang(like)
