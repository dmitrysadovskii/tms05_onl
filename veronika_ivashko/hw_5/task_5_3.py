"""
3. BuzzFuzz
Напишите программу, которая перебирает последовательность от 1 до 100.
Для чисел кратных 3 она должна написать: "Fuzz" вместо печати числа,
а для чисел кратных 5  печатать "Buzz".
Для чисел которые кратны 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.
Вывод должен быть следующим:
1
2
fuzz
4
buzz
fuzz
7
8
"""


def fizz_buzz() -> None:
    """
    Print numbers from 1 to 100:
    - for numbers multiple of 3 and 5 > print fizzbuzz,
    - for numbers multiple of 3 only > print fizz,
    - for nunbers multiple of 5 only > print buzz,
    - number iteself for the others.
    :return: None
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


fizz_buzz()
