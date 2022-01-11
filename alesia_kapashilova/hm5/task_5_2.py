def like(*args):
    if len(args) > 0 and (1072 <= ord(args[0][0].lower()) <= 1103):
        language = 'ru'
    else:
        language = 'en'
    if len(args) == 0:
        print('No one likes this')
    elif len(args) == 1:
        if language == 'en':
            print(f'{args[0]} likes this')
        else:
            print(f'{args[0]} это понравилось')
    elif len(args) == 2:
        if language == 'en':
            print(f'{args[0]} and {args[1]} like this')
        else:
            print(f'{args[0]} и {args[1]} это понравилось')
    elif len(args) == 3:
        if language == 'en':
            print(f'{args[0]}, {args[1]} and {args[2]} like this')
        else:
            print(f'{args[0]}, {args[1]} и {args[2]}  это понравилось')
    else:
        if language == 'en':
            print(f'{args[0]}, {args[1]} and {len(args[2:])} others like this')
        else:
            print(f'{args[0]}, {args[1]} и еще {len(args[2:])} '
                  f'другим понравилось это')
