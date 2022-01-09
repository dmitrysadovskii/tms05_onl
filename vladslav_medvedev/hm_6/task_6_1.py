'''
1.Validate for credit card
Ваша задача написать программу, принимающее число - номер кредитной карты
(число может быть четным или не четным). И проверяющей может ли такая карта
существовать. Предусмотреть защиту от ввода букв, пустой строки и т.д.
validate(4561261212345464) #=> False
validate(4561261212345467) #=> True

4561261212345467 четн
378734493671000 не четн

'''
#Исправить ввод пустой строки и букв !
number_card = input('Please enter number card without space: ')
for i in number_card:
    count = len(number_card)
    if count == 0:
        print("This line is empty, please try again.")
        break
    elif not number_card.isdigit():
        print('You must enter a integer!')
        break
if len(number_card) % 2 == 0:
    count_even = 0
    even_validate = ''
    number_card = number_card +' '
    for i in number_card:
        if i == ' ':
            break
        if number_card[count_even] == i:
            count_even +=2
            new_even = int(i)*2
            if new_even > 9:
                new_even = new_even - 9
            even_validate += str(new_even)
            new_even = 0
        elif number_card[count_even] != i:
            new_even = i
            even_validate += str(new_even)
            new_even = 0
    sum_validate_even = 0
    for i in even_validate:
        i = int(i)
        if i >= 0:
            sum_validate_even += i
    for i in range(1,2):
        if sum_validate_even % 10 == 0:
            print('Card entered correctly! Thank you.')
            break
        else:
            print('Sorry, card entered uncorrectly!')
            break
else:
    count_odd = 1
    odd_validate = ''
    number_card = number_card +' '
    for i in number_card:
        if i == ' ':
            break
        if number_card[count_odd] == i:
            count_odd +=2
            new_odd = int(i)*2
            if new_odd > 9:
                new_odd = new_odd - 9
            odd_validate += str(new_odd)
            new_odd = 0
        elif number_card[count_odd] != i:
            new_odd = i
            odd_validate += str(new_odd)
            new_odd = 0
    sum_validate_odd = 0
    for i in odd_validate:
        i = int(i)
        if i >= 0:
            sum_validate_odd += i
    if sum_validate_odd % 10 == 0:
        print('Card entered correctly! Thank you.')
    else:
        print('Sorry, card entered uncorrectly!')
