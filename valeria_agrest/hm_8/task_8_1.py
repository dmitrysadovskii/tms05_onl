def typed(type):
    def decorator(func):
        def wrapper(*args):
            float_list = []
            str_list = []
            if type == 'int':
                for el in args:
                    float_list.append(float(el))
                return func(*float_list)
            if type == 'str':
                for el in args:
                    str_list.append(str(el))
                return func(*str_list)
        return wrapper
    return decorator


@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c


print(add_three_symbols("3", 5, 0))


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


print(add_two_symbols("3", 5))
