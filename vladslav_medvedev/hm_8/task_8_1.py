'''
Напишите декоратор, который проверял бы тип параметров функции,
конвертировал их если надо и складывал:
@typed(type=’str’)
def add_two_symbols(a, b):
    return a + b

add_two_symbols("3", 5) -> "35"
add_two_symbols(5, 5) -> "55"
add_two_symbols('a', 'b') -> 'ab’

@typed(type=’int’)
def add_three_symbols(a, b, с):
    return a + b + с

add_three_symbols(5, 6, 7) -> 18
add_three_symbols("3", 5, 0) -> 8
add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001
'''


def typed(type):
    def check_accepts(check):
        def new_func(*args):
            arg_list = []
            if type == 'str':
                for i in args:
                    arg_list.append(str(i))
            elif type == 'int':
                for i in args:
                    arg_list.append(float(i))
            return check(*arg_list)
        return new_func
    return check_accepts


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))


@typed(type='int')
def add_three_symbols(a, b, с):
    return a + b + с


print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))
