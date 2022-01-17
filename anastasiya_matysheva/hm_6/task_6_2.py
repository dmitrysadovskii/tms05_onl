
def calc_repeated_char(string):
    count = {}
    for s in string:
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
    return count



def create_result_string(repeated_dict):
    result_string = ""
    for key in repeated_dict:
        if repeated_dict[key] == 1:
            result_string += key
        elif repeated_dict[key] > 1:
            result_string += key
            result_string += str(repeated_dict[key])

    return result_string

def run():
    string = input("Write string : ")
    repeated_char_dict = calc_repeated_char(string)
    result_string = create_result_string(repeated_char_dict)
    return result_string


print(run())
