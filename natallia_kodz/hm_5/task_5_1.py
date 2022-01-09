number1 = 1945
new_list1 = list(str(number1))


def function1():
    number = input("Enter 4-digit number: ")
    new_list = list(str(number))
    if len(new_list) == 4:
        return number
    else:
        print("Incorrect number")
        return function1()


def game():
    num2 = function1()
    new_list2 = list(str(num2))
    bull = 0
    cow = 0
    for i in range(4):
        if new_list1[i] == new_list2[i]:
            bull += 1
        elif new_list2[i] in new_list1:
            cow += 1
    if bull == 4:
        print("Your number is right!!!")
    else:
        print(num2 + " has " + str(bull) + " bulls and " + str(cow) + " cows ")
        return game()


game()
