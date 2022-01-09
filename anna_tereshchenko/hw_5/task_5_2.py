RU = 'ru'
EN = 'en'
dict_word = {
    EN:
        {
            1: 'No one likes this',
            2: 'likes this',
            3: 'and',
            4: 'like this',
            5: 'others like this'
        },
    RU:
        {
            1: 'Никому не понравилось',
            2: 'нравится это',
            3: 'и',
            4: 'нравится это',
            5: 'другим нравится это'
        }
}


def likes(arr, language):
    str1 = EN
    if language == RU:
        str1 = RU
    if not arr:
        print(dict_word[str1][1])
    elif len(arr) == 1:
        print(arr[0], dict_word[str1][2])
    elif len(arr) == 2:
        print(arr[0], dict_word[str1][3], arr[1], dict_word[str1][4])
    elif len(arr) == 3:
        print(f'{arr[0]}, {arr[1]} {dict_word[str1][3]} {arr[2]} {dict_word[str1][4]}')
    else:
        print(f'{arr[0]}, {arr[1]} {dict_word[str1][3]} {len(arr) - 2} {dict_word[str1][5]}')


likes(['Anna', 'Sergey', 'Alex'], EN)
