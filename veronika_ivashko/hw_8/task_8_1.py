"""
Декоратор типов
Напишите декоратор, который проверял бы тип параметров функции, конвертировал
их если надо и складывал:

@typed(input_type='str')
def add_two_symbols(a, b):
    return a + b

add_two_symbols("3", 5) -> "35"
add_two_symbols(5, 5) -> "55"
add_two_symbols('a', 'b') -> 'ab’

@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c

add_three_symbols(5, 6, 7) -> 18
add_three_symbols("3", 5, 0) -> 8
add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001
"""


def typed(input_type):
    """
    Takes all input values and transforms their type according to the type
    specified as 'input_type'. Returns transformed values and uses them as
    input for a function specified in wrapper. Inside the wrapper calls the
    function with previously transformed values.
    :param input_type: specify target type for transformation.
    :return: result of wrapped function.
    """
    def type_decorator(func):
        def wrapper(*args):
            def convert_to_numeric(num):
                """
                Convert input value into integer if it was integer as string,
                convert value into float if it was a float as string, otherwise
                leave original value and type.
                :param num: number of string or float or int type.
                :return: number of int or float type.
                """
                # for integers as strings
                if type(num) is str and num.isdigit():
                    return int(num)
                # for floats as strings
                elif type(num) is str:
                    return float(num)
                # the rest passes without transformations: float/int
                else:
                    return num

            if input_type == 'str':
                args = [str(arg) for arg in args]
            elif input_type == 'int':
                # for numeric transformation take into account format of input
                args = [convert_to_numeric(arg) for arg in args]
            return func(*args)
        return wrapper
    return type_decorator


@typed(input_type='str')
def add_two_symbols(a, b):
    return a + b


print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))


@typed(input_type='int')  # works with both 'int' and 'str' with digits
def add_symbols(*args):
    """
    Perform combining of elements for string input values, sum - for integer
    and/or float input values.
    :param args: digits as integers, floats, strings.
    :return: sum or result of combining strings.
    """
    if len(args) == 0:
        return None
    elif len(args) == 1:
        return args[0]
    else:
        # get type of first element to define type of result variable
        result = args[0]
        for arg in args[1:]:
            result += arg
        return result


print(add_symbols(5, 6, 7))
print(add_symbols("3", 5, 0))
print(add_symbols(0.1, 0.2, 0.4))
print(add_symbols(1, '0.2', 0.4))
print(add_symbols())
print(add_symbols(1))
print(add_symbols('1', 2))
