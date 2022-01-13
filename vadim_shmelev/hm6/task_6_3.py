while True:
    operation_symbol = input("Select operation as symbol (+,-,*,/): ")
    if operation_symbol in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if operation_symbol == '+':
            print("%.2f" % (x+y))
        elif operation_symbol == '-':
            print("%.2f" % (x-y))
        elif operation_symbol == '*':
            print("%.2f" % (x*y))
        elif operation_symbol == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Division by zero is not acceptable!")
    else:
        print("Choose one of four! ")

    break
