"""
1. Перевести строку в массив
"Robin Singh" => ["Robin”, “Singh"]
"I love arrays they are my favorite"
    => ["I", "love", "arrays", "they", "are", "my", "favorite"]
"""


def split_str(some_string: str) -> list:
    return some_string.split()


print(split_str("Robin Singh"))
print(split_str("I love arrays they are my favorite"))
