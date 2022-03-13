alphabet = 'abcdefghijklmnopqrstuvwxyz'


def caesar_encryption(input_string, shift):
    encrypted_string = str()
    for i in input_string:
        place = alphabet.find(i)
        new_place = place + shift
        if i in alphabet:
            encrypted_string += alphabet[new_place]
        else:
            encrypted_string += i
    return encrypted_string


def caesar_decryption(input_string, shift):
    decrypted_string = str()
    for i in input_string:
        place = alphabet.find(i)
        new_place = place - shift
        if i in alphabet:
            decrypted_string += alphabet[new_place]
        else:
            decrypted_string += i
    return decrypted_string


print(caesar_encryption("this is a test string", 5))
print(caesar_decryption("khoor zruog!", 3))
