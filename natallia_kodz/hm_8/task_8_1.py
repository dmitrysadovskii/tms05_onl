def typed(arg_type):
    def wrapper1(func):
        def wrapper2(*args):
            new_args = list()
            for i in args:
                if arg_type == "str":
                    if isinstance(i, str):
                        new_args.append(i)
                    else:
                        new_args.append(str(i))
                elif arg_type == "int":
                    if isinstance(i, int):
                        new_args.append(i)
                    else:
                        new_args.append(float(i))
                else:
                    print("Incorrect arguments type is used")
                    return
            print(func(*new_args))
        return wrapper2
    return wrapper1


@typed(arg_type="str")
def add_two_symbols(a, b):
    return a + b


@typed(arg_type="int")
def add_three_symbols(a, b, c):
    return a + b + c


add_two_symbols("3", 5)
add_two_symbols(5, 5)
add_two_symbols("a", "b")
add_three_symbols(5, 6, 7)
add_three_symbols("3", 5, 0)
add_three_symbols(0.1, 0.2, 0.4)
