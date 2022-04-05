from secrets import choice
from coffee import MENU
from candy import CANDY_MENU 
from resources import resources_coffee
from resources import resources_candy
from resources import resources_meat
from resources import resources_fruit
from resources import resources_veggies
from resources import resources_deli_bread
from resources import resources_pasta_condiments
from resources import resources_dry_goods
from resources import resources_baby_pet_department
from resources import resources_paper_goods
from resources import resources_dairy_department
from resources import resources_frozen_food


profit = 0 


def is_resource_sufficient(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_coffee[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False 
    return is_enough

def is_resource_sufficient_candy(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_candy[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False 
    return is_enough

def process_coins():
    print("Please insert coins. ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total 

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit 
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_coffee[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

def make_candy(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_candy[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

is_on = True 

while is_on: 
    #choice = input("What would you like? (espresso/latte/cappuccino): ")
    name = input("Hi there, what is your name?: ")
    print("\n")
    print(f"Hello {name}, nice to meet you")
    print("Available options: ")
    print("1) Coffee Department, type '1' ")
    print("2) Candy Department, type '2' ")
    print("Type report to view report")
    print("Or, type none to quit") 
    print("\n")
    choice = input("What department would you like to go to today? ")
    #choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "none":
        is_on = False 
    elif choice == "report":
        print("\n") 
        print("Select which department report you would like to view: ")
        print("Coffee Department, type 'coffee_report' ")
        print("Candy Department, type 'candy_report' ")
        print("\n")
        choice_report = input("Choice: ")
        print("\n")
        if choice_report == "coffee_report":
            print(f"Water: {resources_coffee['water']}ml")
            print(f"Milk: {resources_coffee['milk']}ml")
            print(f"Coffee: {resources_coffee['coffee']}g")
            print(f"Money = ${profit}")
            print("\n")

        if choice_report == "candy_report":
            print(f"Sugar: {resources_candy['sugar']}g")
            print(f"Count: {resources_candy['count']} candy bars remaining")
            print("\n")

    if choice == "1":
        print("\n")
        print("Available options: ")
        print("espresso")
        print("latte") 
        print("cappuccino")
        print("\n")
        choice_coffee = input("What would you like to go to buy today? ")

        drink = MENU[choice_coffee]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice_coffee, drink["ingredients"]) 

        check_keep_going = input("Would you like to keep going? Type 'Y' or 'N': ")
        check_keep_going = check_keep_going.lower()
        if check_keep_going == 'y':
            is_on = True
        else:
            is_on = False
    

    if choice == "2":
        print("\n")
        print("Available options: ")
        print("KitKat")
        print("Hersheys") 
        print("Twix")
        print("\n")
        choice_candy = input("What would you like to go to buy today? ")

        candy = CANDY_MENU[choice_candy]
        if is_resource_sufficient_candy(candy["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, candy["cost"]):
                make_candy(choice_candy, candy["ingredients"])  

        check_keep_going = input("Would you like to keep going? Type 'Y' or 'N': ")
        check_keep_going = check_keep_going.lower()
        if check_keep_going == 'y':
            is_on = True
        else:
            is_on = False

