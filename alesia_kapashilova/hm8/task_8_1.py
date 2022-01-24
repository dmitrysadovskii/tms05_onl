def typed(type):
    def conditions_for_data_types(func):
        def wrapper(*args):
            elements_data = []
            assert type in ('str', 'int'), 'Invalid type passed'
            if type == 'str':
                for i in args:
                    elements_data.append(str(i))
            elif type == 'int':
                for i in args:
                    elements_data.append(float(i))
            return func(*elements_data)

        return wrapper

    return conditions_for_data_types


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
