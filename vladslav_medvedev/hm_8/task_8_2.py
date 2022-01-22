"""
Lexicographic increase
На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел (каждое не меньше 0 и не больше 19).
Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в английском языке.
Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2, поскольку слово two в словаре встречается позже слова three, а слово three -- позже слова one (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является истинным)
number_names = {
    	0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    	10: 'ten', 11: 'eleven', 12: 'twelve',
    	13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}

for test_1: 11 1 2 3 4
        el on tw th fo
for test_2: 10 11 12 18 0 3 9
"""
number_names = {
        0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
        10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}

def sort(string):
    for i in range(len(string)):
        string[i] = int(string[i])

    names = []
    for i in string:
        if i in number_names:
            names.append(number_names[i])
    names = sorted(names)
    for i in names:
            print( i )
    if __name__ == '__main__':
        return names


string = input("Enter the numbers separated by a space: ").split()
sort(string)
