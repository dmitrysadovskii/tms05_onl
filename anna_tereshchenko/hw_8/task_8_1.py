def typed(type):
    def decorator(func):
        def wrapper(*args):
            if type == 'int':
                b = []
                for i in args:
                    b.append(float(i))
                return func(*b)
            elif type == 'str':
                c = []
                for i in args:
                    c.append(str(i))
                return func(*c)
            else:
                print('Передан неверный тип')
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
