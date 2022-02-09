a = range(1, 101)
print(type(a))
for number in range(1, 101):
    if number % 3 == 0 and number % 5 != 0:
        print("fuzz")
        continue
    if number % 5 == 0 and number % 3 != 0:
        print("buzz")
        continue
    if number % 3 == 0 and number % 5 == 0:
        print("FuzzBuzz")
        continue
    print(number)
