
"""Ivanou Ivan to Ivan Ivanou task"""

new_string = "Ivanou Ivan"
new_list = new_string.split()
new_list.reverse()
list_to_string = ' '.join([str(elem) for elem in new_list])

print(list_to_string)
