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

money = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01
}

def used_ingredients(name_of_coffee):

    if name_of_coffee == "latte" or name_of_coffee == "cappuccino":
        if resources["water"] < MENU[name_of_coffee]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        elif resources["milk"] < MENU[name_of_coffee]["ingredients"]["milk"]:
            print("Sorry there is not enough milk")
        elif resources["coffee"] < MENU[name_of_coffee]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")

        resources["water"] = resources["water"] - MENU[name_of_coffee]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[name_of_coffee]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[name_of_coffee]["ingredients"]["coffee"]

    elif name_of_coffee == "espresso":
        if resources["water"] < MENU[name_of_coffee]["ingredients"]["water"]:
            print("Sorry there is not enough water")
        elif resources["coffee"] < MENU[name_of_coffee]["ingredients"]["coffee"]:
            print("Sorry there is not enough coffee")

        resources["water"] = resources["water"] - MENU[name_of_coffee]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[name_of_coffee]["ingredients"]["coffee"]



is_on = True
money = 0

while is_on:
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif coffee == "exit":
        is_on = False
    elif coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        used_ingredients(coffee)

# Check resources sufficient?
# Process coins.
# Check transaction successful?
# Make Coffee