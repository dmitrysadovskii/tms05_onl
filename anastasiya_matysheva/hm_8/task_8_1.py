def typed(type):
    def check_accepts(f):
        def new_f(*args):
            argument_list = []
            if type == 'str':
                for i in args:
                    argument_list.append(str(i))
            elif type == 'int':
                for i in args:
                    argument_list.append(float(i))
            return f(*argument_list)
        return new_f
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
