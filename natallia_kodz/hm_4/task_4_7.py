from collections import Counter
text = input('Insert String: ')
line = "".join(ch for ch in text.lower() if ch.isalpha())
print(sorted(Counter(line).items(), key=lambda x: (-x[1], x[0]))[0][0])
