print('''
Please choose the math operation:
+ for addition
- for subtraction
* for multiplication
/ for division
''')


def is_operation_supported(operation):
    supported_operation = set("+-*/")
    support = False
    for i in supported_operation:
        if operation == i:
            support = True
    return support


def calculator():
    operation = input('Enter the math operation: ')
    if is_operation_supported(operation):
        numb_1 = float(input('Enter first number: '))
        numb_2 = float(input('Enter first number: '))

        if numb_2 == 0 and operation == '/':
            print('Division by 0!')
        elif operation == '+':
            print(numb_1 + numb_2)
        elif operation == '-':
            print(numb_1 - numb_2)
        elif operation == '*':
            print(numb_1 * numb_2)
        elif operation == '/':
            print(numb_1 / numb_2)
    else:
        print('Unsupported operation')


calculator()
