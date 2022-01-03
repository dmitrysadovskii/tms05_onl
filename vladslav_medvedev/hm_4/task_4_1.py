"""
Перевести строку в массив
"Robin Singh" => ["Robin”, “Singh"]
"I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
"""
f_str = "Robin Singh"
s_str = "I love arrays they are my favorite"

f_result = f_str.split()
s_result = s_str.split()

print(f_result)
print(s_result)
