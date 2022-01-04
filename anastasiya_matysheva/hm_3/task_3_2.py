Words = input('Enter words:')
commands = Words.split()
a = [f'{w}ing' for w in commands]
print(' '.join(a))
