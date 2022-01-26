
"""Function that takes arguments and depending on the type of arg (string
or float), it uses one method .apppend.
Because of difference in type of arg, the results will be different"""
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

add_two_symbols("3", 5)
add_two_symbols(5, 5)
add_two_symbols('a', 'b')

@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c

add_three_symbols(5, 6, 7)
add_three_symbols("3", 5, 0)
add_three_symbols(0.1, 0.2, 0.4)
