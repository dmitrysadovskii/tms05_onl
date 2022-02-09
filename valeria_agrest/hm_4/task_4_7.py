str1 = 'How do you do?'
lower_string = str1.lower()
letters = ''.join(filter(str.isalpha, lower_string))

unique_set = set(sorted(list(letters)))

most_common = None
qty_most_common = 0

for item in unique_set:
    qty = letters.count(item)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = item

print(most_common)
