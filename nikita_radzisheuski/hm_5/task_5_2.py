"""HOMEWORK TASK NUMBER TWO
THIS CODE IS A "LIKE" GAME
WITH TWO LANGS: EN, RU
"""

from langdetect import detect

names = ['Mike', 'Nick', 'Lucas', 'Danil',
         'Fedorro', 'Jack']
others = names[2:]
names_lang = detect(str(names))


def lang_choosing(names_lang):
    if names_lang == 'en':
        names_likes_en(names, others)
    elif names_lang == 'ru':
        names_likes_ru(names, others)
    else:
        print('LOL! The Lang is out of scope')


def names_likes_ru(names, others):
    if len(names) < 1:
        print("Никому не нравится!")
    elif len(names) >= 3:
        print(f'{names[0]}, {names[1]} и '
              f'{len(others)} другим нравится это')
    elif len(names) >= 3:
        print(f'{names[0]}, {names[1]} и {names[2]} нравится это')
    elif len(names) >= 2:
        print(f'{names[0]} и {names[1]} нравится это')
    elif len(names) == 1:
        print(names, "нравится это")
    pass


def names_likes_en(names, others):
    if len(names) < 1:
        print("No one likes this")
    elif len(names) >= 3:
        print(f'{names[0]}, {names[1]} and '
              f'{len(others)} others like this')
    elif len(names) >= 3:
        print(f'{names[0]}, {names[1]} and {names[2]} like this')
    elif len(names) >= 2:
        print(f'{names[0]} and {names[1]} like this')
    elif len(names) == 1:
        print(names, "likes this")


lang_choosing(names_lang)
