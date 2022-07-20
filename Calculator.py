print('''

           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   
 ''')

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide
    }

first_number = int(input("What's the first number?: "))

for symbol in operations:
    print(symbol)

chosen_operation = input("Pick an operation from the line above: ")
second_number = int(input("What's the next number?: "))
result = operations[chosen_operation]
result = result(first_number, second_number)
print(f"{first_number} {chosen_operation} {second_number} = {result}")
decision = input(f"Type 'y' to continue calculating witch {result}, or type 'n' to start a new calculation: ")