"""
2. Подсчет количества букв
На вход подается строка, например, "cccbba"
результат работы программы - строка “c3b2a"

Примеры для проверки работоспособности:
"cccbba" == "c3b2a"
"abeehhhhhccced" == "abe2h5c3ed"
"aaabbceedd" == "a3b2ce2d2"
"abcde" == "abcde"
"aaabbdefffff" == "a3b2def5"
"""


def compress_string(some_string: str) -> str:
    """
    Compresses a string due to the logic: if there are any duplicated elements,
    which follow each other, the element will be written with the number of
    such elements in the sequence. If sequence is interrupted, new element will
    be written and length of this new sequence will be calculated and written.
    If element has no following duplicates, 1 will be omitted, and only the
    element itself will be written, then the algorithm switches to the next
    element.
    :param some_string: any string or text.
    :return: string with elements followed by number of their occurrences.
    """
    result = ''
    counter = 1
    for i in range(len(some_string)):
        # write new element if previous sequence was interrupted
        if counter == 1:
            result += some_string[i]

        # check the sequence duration
        if i != len(some_string) - 1:  # for all elements but the last
            # check next element if sequence may continue
            if some_string[i + 1] == some_string[i]:
                counter += 1
            # sequence is interrupted, write counter if element was multiplied
            elif counter > 1:
                result += str(counter)
                counter = 1
        elif counter > 1:  # for the last only, if element was multiplied
            result += str(counter)
    return result


print(compress_string("cccbba"))
print(compress_string("abeehhhhhccced"))
print(compress_string("aaabbceedd"))
print(compress_string("abcde"))
print(compress_string("aaabbdefffff"))
