def card_number_validation(card_number):
    if len(str(card_number)) < 11 or len(str(card_number)) > 16:
        return "Number should consist of more than 10 and less than 20 digits"
    elif set(str(card_number)) <= set('0123456789'):
        digits_list = []
        for i in str(card_number):
            digits_list.append(int(i))
        if len(str(card_number)) % 2 == 0:
            for x in range(0, len(str(card_number)), 2):
                digits_list[x] = digits_list[x] * 2
                if digits_list[x] > 9:
                    digits_list[x] = digits_list[x] - 9
                else:
                    continue
        else:
            for x in range(1, len(str(card_number)), 2):
                digits_list[x] = digits_list[x] * 2
                if digits_list[x] > 9:
                    digits_list[x] = digits_list[x] - 9
                else:
                    continue
        if sum(digits_list) % 10 == 0:
            return "Card number is valid"
        else:
            return "Card number is invalid"
    else:
        return "Incorrect symbols in number, try again please"


print(card_number_validation(4222222222222))
