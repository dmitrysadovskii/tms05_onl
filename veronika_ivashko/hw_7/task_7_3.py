"""
2) Необходимо составить список чисел которые указывают на длину слов в строке:
sentence = " thequick brown fox jumps over the lazy dog",
но только если слово не "the".
"""


def get_words_length(some_string: str) -> list:
    """
    For some input string function splits the text into the words and counts
    the length of the word if the word is not equal to 'the' or has any letter
    inside itself.
    :param some_string: some string with elements containing letters.
    :return: list of numbers identifying the length of each word.
    """
    return [len(word) for word in some_string.split() if word != 'the'
            and any([symbol.isalpha() for symbol in word])]


print(get_words_length(" thequick brown fox jumps over the lazy dog"))
print(get_words_length(" thequick brown fox jumps over -  the lazy dog !"))
print(get_words_length(" thequick brown fox jumps over the lazy dog - "
                       "Archi-the-dog"))
