"""
Function to encode or decode text using Caesar Cipher
It works with upper and lower characters and commas, spaces etc.
Some info for tests:
Replace num = 3: hello world! -> khoor zruog!
Replace num = -3: khoor zruog! -> hello world!
Replace num = 5: this is a test string -> ymnx nx f yjxy xywnsl
Replace num = -5: ymnx nx f yjxy xywnsl -> this is a test string
"""


def encode_text(replace_num, text):
    encode = ""
    decode = ""
    for i in text:
        if i.isupper():
            """Find character number in unicode"""
            i_index = ord(i) - ord("A")
            """Caesar Cipher mathematically is c = (x + n) % 26"""
            if replace_num > 0:
                changed_index = (i_index + replace_num) % 26
                changed_unicode = changed_index + ord("A")
                changed_character = chr(changed_unicode)
                encode = encode + changed_character
            elif replace_num < 0:
                changed_index = (i_index - -replace_num) % 26
                changed_unicode = changed_index + ord("A")
                changed_character = chr(changed_unicode)
                decode = decode + changed_character
        elif i.islower():
            i_index = ord(i) - ord("a")
            if replace_num > 0:
                changed_index = (i_index + replace_num) % 26
                changed_unicode = changed_index + ord("a")
                changed_character = chr(changed_unicode)
                encode = encode + changed_character
            elif replace_num < 0:
                changed_index = (i_index - -replace_num) % 26
                changed_unicode = changed_index + ord("a")
                changed_character = chr(changed_unicode)
                decode = decode + changed_character
        else:
            if replace_num > 0:
                encode += i
            if replace_num < 0:
                decode += i
    print(f"Entered text: {text}")
    print(f"Encoded/decoded text: {encode}{decode}")


encode_text(int(input("Please enter length of sdvig"
                      " (Enter positive num to Encode"
                      " or negative to Decode): ")),
            input("Please enter your text here: "))
