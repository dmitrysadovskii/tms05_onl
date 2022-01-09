from collections import Counter
import re


def find_frequent_letter(text):
    opt = re.sub(r'[^\w\s]', '', text)
    opt = str(opt).lower()
    ct = Counter(opt)
    most_commons = ct.most_common(1)
    most_frequent = most_commons[0]
    return most_frequent[0]


if __name__ == "__main__":
    a = find_frequent_letter('a-z')
    print(a)
    b = find_frequent_letter('HelLo WorLd!')
    print(b)
    c = find_frequent_letter('How do you do?')
    print(c)
    d = find_frequent_letter('One')
    print(d)
    e = find_frequent_letter('HAAaooo!!!!?')
    print(e)
    f = find_frequent_letter('a' * 9000 + 'b' * 1000)
    print(f)
