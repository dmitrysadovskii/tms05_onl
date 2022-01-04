Words = input('Enter words:')
commands = Words.split()
arr = [f'{w}ing' for w in commands]
print(' '.join(arr))

