"""HOMEWORK TASK NUMBER THREE
THIS CODE IS A BUZZFUZZ GAME
"""

list_of_nums = list(range(1, 100))


def buzz_fuzz(list_of_nums):
    for i in list_of_nums:
        if i % 3 == 0:
            print("Fuzz")
            continue
        elif i % 5 == 0:
            print("Buzz")
            continue
        elif i % 3 == 0 and i % 5 == 0:
            print("FuzzBuzz")
            continue
        print(i)


buzz_fuzz(list_of_nums)
