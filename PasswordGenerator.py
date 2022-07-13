import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""

print("Welcome to the PyPassword Generator!")
numb_letters = int(input("How many letters would you like in your password? \n"))
for let in range(numb_letters):
    password += random.choice(letters)
numb_symbols = int(input("How many symbols would you like? \n"))
for sym in range(numb_symbols):
    password += random.choice(symbols)
numb_numbers = int(input("How many numbers would you like? \n"))
for num in range(numb_numbers):
    password += random.choice(numbers)

print(password)
