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

money = 0


def check_ingredients(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coin():
    print("Please insert coins.")
    total = float(input("How many quarters: ")) * 0.25
    total += float(input("How many dimes: ")) * 0.10
    total += float(input("How many nickles: ")) * 0.05
    total += float(input("How many pennies: ")) * 0.01
    return total


def transaction(order_cost, total):
    if total > order_cost:
        change = round(total - order_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += order_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True
while is_on:

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")

    elif choice == "off":
        is_on = False

    elif choice in ["espresso", "latte", "cappuccino"]:
        drink = MENU[choice]
        if check_ingredients(drink["ingredients"]):
            payment = process_coin()
            money += payment
            if transaction(drink["cost"], payment):
                make_coffee(choice, drink["ingredients"])

