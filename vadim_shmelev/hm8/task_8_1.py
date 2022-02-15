def typed(type):
    def accept(f):
        def new_func(*args):
            argument_list = []
            if type == 'str':
                for i in args:
                    argument_list.append(str(i))
            elif type == 'int':
                for i in args:
                    argument_list.append(float(i))
            return f(*argument_list)
        return new_func
    return accept


@typed(type='str')
def add_two_numbs(a, b):
    return a + b


print(add_two_numbs("3", 5))
print(add_two_numbs(5, 5))
print(add_two_numbs('a', 'b'))


@typed(type='int')
def add_three_numbs(a, b, с):
    return a + b + с


print(add_three_numbs(5, 6, 7))
print(add_three_numbs("3", 5, 0))
print(add_three_numbs(0.1, 0.2, 0.4))
