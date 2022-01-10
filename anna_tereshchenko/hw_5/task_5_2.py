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


def likes(arr):
    str1 = EN
    for i in arr:
        for j in i:
            if ord(j) in range(1040, 1104):
                str1 = RU
            break
        break
    if not arr:
        print(dict_word[str1][1])
    elif len(arr) == 1:
        print(arr[0], dict_word[str1][2])
    elif len(arr) == 2:
        print(arr[0], dict_word[str1][3], arr[1], dict_word[str1][4])
    elif len(arr) == 3:
        print(f'{arr[0]}, {arr[1]} {dict_word[str1][3]} '
              f'{arr[2]} {dict_word[str1][4]}')
    else:
        print(f'{arr[0]}, {arr[1]} {dict_word[str1][3]} '
              f'{len(arr) - 2} {dict_word[str1][5]}')


likes(['Анна', 'Алексей', 'Евгений'])
