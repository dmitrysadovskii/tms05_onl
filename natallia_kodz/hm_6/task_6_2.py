def letters_count(word):
    letters_dict = {}
    for i in word:
        letters_dict[i] = word.count(i)
    letters_string = "".join([f"{key}{value}" for key, value
                             in letters_dict.items()])
    result = letters_string.replace("1", "")
    return result


print(letters_count("kkkertgg"))
