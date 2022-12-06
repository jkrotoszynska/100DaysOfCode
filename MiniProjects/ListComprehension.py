numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Angela"
letters = [letter for letter in name]
print(letters)

double = [num * 2 for num in range(1,5)]
print(double)

names = ["Alex", "Beth", "Dave", "Caroline", "Angela", "Dan"]
short_names = [name for name in names if len(name) < 5]
print(short_names)