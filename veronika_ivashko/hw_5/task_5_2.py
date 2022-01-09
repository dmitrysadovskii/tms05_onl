"""
2. Like
Создайте программу, которая, принимая массив имён,
возвращает строку описывающая количество лайков (как в Facebook).

Примеры:
likes() -> "no one likes this"
likes("Ann") -> "Ann likes this"
likes("Ann", "Alex") -> "Ann and Alex like this"
likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this"
likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this"

Бонусные очки
Функция работает на нескольких языках - язык ответа определяется
по языку входного массива.
"""


def likes(*args: str) -> str:
    """
    Make up a text which users like some objects based on the names provided.
    :param args: names of users
    :return: string
    """
    # identify the language
    # if any name is provided and starts with 'ru' ascii codes > 'ru'
    if len(args) > 0 and (1072 <= ord(args[0][0].lower()) <= 1103):
        language = 'ru'
    else:
        language = 'en'

    # make up a phrase
    if len(args) == 0:
        phrase = 'no one likes this'
    elif len(args) == 1:
        if language == 'en':
            phrase = f'{args[0]} likes this'
        else:
            # в русском сложно подобрать обезличенные глаголы, перефразировала
            phrase = f'{args[0]} рекомендует это'
    elif len(args) == 2:
        if language == 'en':
            phrase = f'{args[0]} and {args[1]} like this'
        else:
            phrase = f'{args[0]} и {args[1]} говорят, что им нравится это'
    elif len(args) == 3:
        if language == 'en':
            phrase = f'{args[0]}, {args[1]} and {args[2]} like this'
        else:
            phrase = f'{args[0]}, {args[1]} и {args[2]} ' \
                     f'говорят, что им нравится это'
    else:
        if language == 'en':
            phrase = f'{args[0]}, {args[1]} and {len(args[2:])} ' \
                     f'others like this'
        else:
            phrase = f'{args[0]}, {args[1]} и еще {len(args[2:])} человека ' \
                     f'говорят, что им нравится это'
    return phrase


print(likes())
print(likes("Ann"))
print(likes("Ann", "Alex"))
print(likes("Ann", "Alex", "Mark"))
print(likes("Ann", "Alex", "Mark", "Max"))
print(likes('Маша'))
print(likes("Маша", "Андрей"))
print(likes("Маша", "Андрей", "Полина"))
print(likes("Маша", "Андрей", "Полина", "Максим"))
