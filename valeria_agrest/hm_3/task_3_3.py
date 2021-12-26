d = 'Ivanou Ivan'


def rev1(s):
    print(len(s))
    print(s[7:12], s[:7])


def rev2(s):
    words = s.split(' ')
    reverse_str = ' '.join(reversed(words))
    print(reverse_str)


rev1(d)
rev2(d)
