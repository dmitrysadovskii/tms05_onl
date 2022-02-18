numb_names = {
    0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six",
    7: "seven", 8: "eight", 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
    17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}


def numbers_sorting(func):
    def wrapper(*args):
        numb_list1 = func(*args)
        numb_names1 = list()
        for i in numb_list1:
            numb_names1.append(numb_names[int(i)])
        sorted_numb_names1 = sorted(numb_names1)
        sorted_numb_list1 = list()
        for x in sorted_numb_names1:
            for y in numb_names:
                if x == numb_names[y]:
                    sorted_numb_list1.append(y)
        result = " ".join(map(str, sorted_numb_list1))
        print(result)
    return wrapper


@numbers_sorting
def numbers(numb_string):
    numbers_list = numb_string.split()
    for i in numbers_list:
        if int(i) < 0 or int(i) > 19:
            print("Numbers should be in [0, 19]")
            exit()
        else:
            continue
    if len(numbers_list) > 100:
        print("numbers_string should contain no more than 100 numbers")
        exit()
    else:
        return numbers_list


numbers("0 5 7 9 19 10 7 11 15")
