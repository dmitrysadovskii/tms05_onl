"""
Шифр цезаря
Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ
заменяется другим, отстоящим от него в алфавите на фиксированное число позиций.

Примеры:
hello world! -> khoor zruog!
this is a test string -> ymnx nx f yjxy xywnsl

Напишите две функции - encode и decode принимающие как параметр строку и
число - сдвиг.

Бонусные очки
1. Шифр работает на нескольких языках (русский, английский, etc.)
2. Шифр сохраняет исходный регистр и знаки препинания
3. Можно ли обойтись одной функцией для зашифровки и дешифровки?
4. Придумайте свой шифр
"""


def caesar_cipher(message: str, shift: int) -> str:
    """
    Transforms input message according to the shift specified, for each element
    identifies the alphabet if it exists, numbers are also transformed
    according to the shift specified. Algorythm works both sides: for
    encryption and decryption. Shift can be negative. To decrypt already
    encrypted message - use encrypted message as input message and provide the
    shift with the opposite sign, for example: if message was encrypted with
    shift equal to 5, provide shift equal to -5 to decrypt it.
    :param message: some text to encrypt.
    :param shift: number of elements in the alphabet to shift.
    :return: encrypted / decrypted message.
    """
    languages = {
        'en': [chr(i) for i in range(ord('a'), ord('z')+1)],
        'rus': [chr(i) for i in range(ord('а'), ord('я')+1)]
    }
    range_of_numbers = [str(i) for i in range(10)]

    # transforms each symbol according to its alphabet or range of values
    def get_new_symbol(old_symbol: str, values_to_transform: list,
                       shift_num: int) -> str:
        """
        Encrypt or decrypt specified symbol due to possible values and
        provided shift. For each symbol a new range of values can be specified.
        :param old_symbol: symbol to encrypt / decrypt.
        :param values_to_transform: alphabet or numbers or another values.
        :param shift_num: number of elements to move.
        :return: encrypted / decrypted symbol.
        """
        is_upper = old_symbol.isupper()
        old_symbol = old_symbol.lower()
        if old_symbol in values_to_transform:
            new_index = values_to_transform.index(old_symbol) + shift_num
            # when new index overlaps possible range
            if abs(new_index) > len(values_to_transform) - 1:
                remainder = abs(new_index) % len(values_to_transform)
                # check and define direction of new_index
                if new_index < 0:
                    new_index = -remainder
                else:
                    new_index = remainder
            old_symbol = values_to_transform[new_index]
        if is_upper:
            old_symbol = old_symbol.upper()
        return old_symbol

    new_message = ''
    for symbol in message:
        # identify the alphabet to use
        check_language = [symbol.lower() in alpha for alpha
                          in languages.values()]
        if any(check_language):
            language_index = check_language.index(True)
            language_encoding = list(languages.keys())[language_index]
        else:
            # when language is not identified > 'en'> no transformation
            language_encoding = 'en'
        alphabet = languages.get(language_encoding)
        # transform the symbol
        if symbol in range_of_numbers:
            symbol = get_new_symbol(symbol, range_of_numbers, shift)
        elif symbol.lower() in alphabet:
            symbol = get_new_symbol(symbol, alphabet, shift)
        # if symbol is not found > remains the same
        new_message += symbol
    return new_message


# print(caesar_cipher('  2  hi - , W woRLldza', -5))
# print(caesar_cipher('а    фhi - , W woRLldza ! привет moy svet', -65))

original_message = 'Привет moy svet!'
encrypted_message = caesar_cipher(original_message, 5)
decrypted_message = caesar_cipher(encrypted_message, -5)
print(f'Original message: {original_message}')
print(f'Encrypted message: {encrypted_message}')
print(f'Decrypted message: {decrypted_message}')
