def typed(type):
    def decorator(func):
        def wrapper(*args):
            casted_args = []
            assert type in ('int', 'str'), 'Передан неверный тип'
            if type == 'int':
                for i in args:
                    casted_args.append(float(i))
            elif type == 'str':
                for i in args:
                    casted_args.append(str(i))
            return func(*casted_args)
        return wrapper
    return decorator


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


print(add_two_symbols("3.0", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))


@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c


print(add_three_symbols(5.0, 6, 7))
print(add_three_symbols("3.0", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))
