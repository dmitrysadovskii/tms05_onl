"""
3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
сделайте из него строку => "I love arrays they are my favorite"
"""


def get_str_from_list(some_list: list) -> str:
    return ' '.join(some_list)


print(get_str_from_list(["I", "love", "arrays",
                         "they", "are", "my", "favorite"]))
