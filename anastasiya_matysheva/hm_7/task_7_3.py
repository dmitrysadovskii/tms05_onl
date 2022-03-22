def cezar_code(string, number, dec, lang):
    alpha_en = 'abcdefghijklmnopqrstuvwxyz'
    alpha_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''
    if dec == 'enc':
        if lang == 'ru':
            for c in string:
                result += \
                    alpha_ru[(alpha_ru.index(c) + number) % len(alpha_ru)]
        elif lang == 'en':
            for c in string:
                result += \
                    alpha_en[(alpha_en.index(c) + number) % len(alpha_en)]
    else:
        if lang == 'ru':
            for c in string:
                result += \
                    alpha_ru[(alpha_ru.index(c) - number) % len(alpha_ru)]
        elif lang == 'en':
            for c in string:
                result += \
                    alpha_en[(alpha_en.index(c) - number) % len(alpha_en)]
    return result


print(cezar_code(input('Enter world: '), int(input('Enter the step: ')),
                 input('Choose decode or encode (enter "dec" or "enc"): '),
                 input('Choose english or russian (enter "en" or "ru"); ')))
