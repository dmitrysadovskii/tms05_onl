"""Task with * number one"""
import functools
import operator

a = [1, 5, 2, 9, 2, 9, 1]
ab = functools.reduce(operator.xor, a)
print(ab)
