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


def check_ingredients(order_option):
    """
    Checks if there is enough ingredients to make the coffe
    """

    order_ingredients = MENU[order_option]['ingredients']

    enough_ingredients = True

    for ing in order_ingredients:
        if order_ingredients[ing] > resources[ing]:
            print(f"Sorry there is not enough {ing}")
            enough_ingredients = False

    return enough_ingredients


def process_coin(order_option):

    """
    Does everything related to money.
    Calculates the inserted value
    Verifies if it's enough
    Inserts the coffe cost to the machine profit
    Returns the extra amount to the user
    """

    global profit

    print("\nPlease insert coins.")
    money_inserted = float(input("How many quarters?: ")) * 0.25
    money_inserted += float(input("How many dimes?: ")) * 0.10
    money_inserted += float(input("How many nickles?: ")) * 0.05
    money_inserted += float(input("How many pennies?: "))* 0.01

    profit += money_inserted

    if money_inserted < MENU[order_option]['cost']:
        print("Sorry, there is not enough money. Money refunded\n")
        profit -= money_inserted

        return False #skip the coffe maker function

    else:
        coffe_cost = MENU[order_option]["cost"]

        if money_inserted > coffe_cost:
            refund = money_inserted - coffe_cost
            profit -= refund
            print(f"\n{order_option.title()} costs ${coffe_cost:.2f} and you inserted ${money_inserted:.2f}.")
            print(f"Here is ${refund:.2f} in change")

        return True #let the coffee be made



def coffe_maker(order_option):
    """
    Make the coffee and subtract the ingredients used
    """

    ingredients = MENU[order_option]['ingredients']

    for i in ingredients:
        resources[i] -= ingredients[i]

    return print(f"Here is your {order_option} ☕ Enjoy!\n")




finish_program = False
profit = 0
possibles = ['espresso', 'latte','cappuccino','report','off']



while finish_program is False:

    option = input("\nWhat would you like ? (espresso/latte/cappuccino): ").lower()

    # avoid miss types...
    if option not in possibles:
        print("Please try again\n")

    # stops the loop
    elif option == 'off':
        print(f"Total money made: ${profit:.2f}")
        finish_program = True

    # show the currently resources
    elif option == 'report':
        print(f"\n"
              f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffe: {resources['coffee']}ml\n"
              f"Money: ${profit:.2f}\n")


    # check if there is enough ingredients before making the coffee
    elif check_ingredients(option) != False:
        #check if the money is ok to proceed
        if process_coin(option) != False:
            coffe_maker(option)