def letters_count(your_word):
    list_letter = {}
    for y in your_word:
        list_letter[y] = your_word.count(y)
    new_letter = "".join([f"{key}{value}" for key, value
                          in list_letter.items()])
    result = new_letter.replace("1", "")
    return result


your_latter = input('Enter a set of letters:')
print(letters_count(your_latter))
