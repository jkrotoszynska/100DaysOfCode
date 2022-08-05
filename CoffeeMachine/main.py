MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_ingredients(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")


def process_coin():
    print("Please insert coins.")
    total = input("How many quarters: ") * 0.25
    total += input("How many dimes: ") * 0.10
    total += input("How many nickles: ") * 0.05
    total += input("How many pennies: ") * 0.01
    return total

#def transaction():

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
money = 0


while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif choice == "exit":
        is_on = False
    elif choice in ["espresso", "latte", "cappuccino"]:
        drink = MENU[choice]
        check_ingredients(drink["ingredients"])
        process_coin()
        #transaction()
        make_coffee(choice, drink["ingredients"])

