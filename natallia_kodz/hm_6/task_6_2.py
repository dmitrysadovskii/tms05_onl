def letters_count(word):
    word_list = list(word)
    letters_string = ""
    count = 1
    for i in range(len(word_list) - 1):
        if word_list[i + 1] == word_list[i]:
            count += 1
        else:
            letters_string += f"{word_list[i]}{count}"
            count = 1
    if word_list[-1] == word_list[-2]:
        letters_string += f"{word_list[-1]}{count}"
    else:
        letters_string += f"{word_list[-1]}1"
    result = letters_string.replace("1", "")
    return result


print(letters_count("kkkertggk"))
