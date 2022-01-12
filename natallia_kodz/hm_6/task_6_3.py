def calculator(act, num1, num2):
    if int(act) == 4 and int(num2) == 0:
        return "Division by 0 is not allowed"
    elif int(act) == 1:
        addition_result = int(num1) + int(num2)
        return f"Result: {addition_result}"
    elif int(act) == 2:
        subtraction_result = int(num1) - int(num2)
        return f"Result: {subtraction_result}"
    elif int(act) == 3:
        multiplication_result = int(num1) * int(num2)
        return f"Result: {multiplication_result}"
    elif int(act) == 4:
        division_result = int(num1) // int(num2)
        remainder = int(num1) % int(num2)
        return f"Result: {division_result}, Remainder: {remainder}"
    else:
        return "There is no such menu number"


action = input("Choose action:\n 1. Addition\n 2. Subtraction\n"
               " 3. Multiplication\n 4. Division\nEnter menu number: ")
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
print(calculator(action, number1, number2))
