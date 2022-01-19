def generate_sequnce():

    count = 0
    world_index = []
    sorted_names = {}

    number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

    for i in number_names.values():
        world_index.append(i)
    world_index.sort()
    for i in world_index:
        sorted_names[count] = i
        count += 1
    value_list = list(number_names.values())
    result_list = []
    for i in range(len(world_index)):
        result_list.append(value_list.index(world_index[i]))
    return result_list


def func(input_list):
    ev = generate_sequnce()
    for i in range(len(input_list) - 1):
        for j in range(len(input_list) - i - 1):
            if ev.index(input_list[j]) > ev.index(input_list[j] + 1):
                input_list[j], input_list[j + 1] = input_list[j + 1],\
                                                   input_list[j]

    return input_list


def get_input():
    s = input("Enter the numbers separated by a space : ")
    item_list = s.split()
    int_list = [int(i) for i in item_list]
    result = func(int_list)
    return result


print(get_input())
