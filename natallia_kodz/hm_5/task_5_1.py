number1 = 1945
new_list1 = list(str(number1))


def get_user_number():
    number = input("Enter 4-digit number: ")
    if len(set(number)) < len(number):
        print("Digits in number should be unique")
        return get_user_number()
    elif len(list(number)) == 4:
        return number
    else:
        print("Incorrect number")
        return get_user_number()


def game():
    num2 = get_user_number()
    new_list2 = list(num2)
    bull = 0
    cow = 0
    for i in range(len(new_list2)):
        if new_list2[i] == new_list1[i]:
            bull += 1
        elif new_list2[i] in new_list1:
            cow += 1
    if bull == 4:
        print("Your number is right!!!")
    else:
        print(f"{num2} has {bull} bulls and {cow} cows")
        return game()


game()
