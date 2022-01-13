'''
Простейший калькулятор v0.1
Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет произвести над числами,
а затем запрашивает два числа и выводит результат
Проверка деления на 0.
Пример
Выберите операцию:
    1. Сложение
    2. Вычитание
    3. Умножение
    4. Деление
'''
result_validate_one, result_validate_two = 0, 0


def validate(variable_number_one,variable_number_two,result_validate_one,
             result_validate_two):
    if variable_number_one != ' ' and not variable_number_one.isdigit():
        print('The first number was entered incorrectly!')
    else :
         result_validate_one += 1
         print('The first number is entered correctly!')

    if variable_number_two != ' ' and not variable_number_two.isdigit():
        print('The second number is entered incorrectly!')
    else:
        print('The second number is entered correctly')
        result_validate_two += 1
    return result_validate_one, result_validate_two


def calculator(operation, variable_number_one, variable_number_two):
    if int(operation) == 4 and int(variable_number_two) == 0:
        return "Division by 0 is not allowed"
    elif int(operation) == 1:
        addition = int(variable_number_one) + int(variable_number_two)
        return f"Result: {addition}"
    elif int(operation) == 2:
        subtraction = int(variable_number_one) - int(variable_number_two)
        return f"Result: {subtraction}"
    elif int(operation) == 3:
        multiplication = int(variable_number_one) * int(variable_number_two)
        return f"Result: {multiplication}"
    elif int(operation) == 4:
        division = int(variable_number_one) // int(variable_number_two)
        return f"Result: {division}"
    else:
        return "There is no such menu number"


operation = input("Choose an operation:"
                  "\n1.Addition"
                  "\n2.Subtraction"
                  "\n3.Multiplication"
                  "\n4.Division\n")
variable_number_one = input("Enter the first number: ")
variable_number_two = input("Enter the second number: ")
num_for_validate_one, num_for_validate_two = validate(variable_number_one,
                                                      variable_number_two,
                                                      result_validate_one,
                                                      result_validate_two)
sum_num_for_validate = num_for_validate_one + num_for_validate_two
if  sum_num_for_validate == 2:
    print(calculator(operation, variable_number_one, variable_number_two))
else:
    print('Numbers entered incorrectly')
