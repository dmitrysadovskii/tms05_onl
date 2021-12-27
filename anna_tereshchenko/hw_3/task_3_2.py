word = input('Type a word:')
commands = word.split()
arr = [f'{w}ing' for w in commands]
print(' '.join(arr))
