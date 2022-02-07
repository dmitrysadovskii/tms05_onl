def calculator():
    operations = ('+', '-', '*', '/', '=')
    operation = input("select the type of mathematical operation:"
                      " + ; - ; * ; / ; = - if complex expression:")
    if operation not in operations:
        print('choose one operation from the suggested ones!')
    if operation in ('+', '-', '*', '/'):
        x = float(input("first numb:"))
        y = float(input("second numb:"))
        if operation == '+':
            print(x + y)
        elif operation == '-':
            print(x - y)
        elif operation == '*':
            print(x * y)
        elif operation == '/':
            print(x / y)
    elif operation == '=':
        args = input("Enter expression:")
        print(eval(args))


calculator()
