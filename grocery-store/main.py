from secrets import choice
from coffee import MENU
from candy import CANDY_MENU 
from meat import MEAT_MENU
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

def is_resource_sufficient_meat(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_meat[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False 
    return is_enough

def is_resource_sufficient_fruit(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_fruit[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False 
    return is_enough

def is_resource_sufficient_veggies(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_veggies[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False 
    return is_enough

def is_resource_sufficient_deli_bread(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_deli_bread[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False 
    return is_enough

def is_resource_sufficient_pasta_condiments(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_pasta_condiments[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False 
    return is_enough

def is_resource_sufficient_dry_goods(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_dry_goods[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False 
    return is_enough

def is_resource_sufficient_baby_pet_department(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_baby_pet_department[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False 
    return is_enough

def is_resource_sufficient_paper_goods(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_paper_goods[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False 
    return is_enough

def is_resource_sufficient_dairy_department(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_dairy_department[item]:
            print(f"Sorry there is not enough {item}. ")
            is_enough = False 
    return is_enough

def is_resource_sufficient_frozen_food(order_ingredients):
    is_enough = True 
    for item in order_ingredients:
        if order_ingredients[item] >= resources_frozen_food[item]:
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

def make_meat(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_meat[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

def make_fruit(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_fruit[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

def make_veggies(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_veggies[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

def make_deli_bread(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_deli_bread[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

def make_pasta_condiments(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_pasta_condiments[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

def make_dry_goods(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_dry_goods[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

def make_baby_pet_department(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_baby_pet_department[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

def make_paper_goods(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_paper_goods[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

def make_dairy_department(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_dairy_department[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ")

def make_frozen_food(drink_name, order_ingredients):
    for item in order_ingredients:
        resources_frozen_food[item] -= order_ingredients[item]
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
    print("3) Meat Department, type '3' ") 
    print("4) Fruit Department, type '4' ") 
    print("5) Veggies Department, type '5' ") 
    print("6) Deli Bread Department, type '6' ") 
    print("7) Pasta Condiments Department, type '7' ") 
    print("8) Dry Goods Department, type '8' ") 
    print("9) Baby Pet Department, type '9' ") 
    print("10) Paper Goods Department, type '10' ") 
    print("11) Dairy Department, type '11' ") 
    print("12) Frozen Fruit Department, type '12' ") 
    print("Type report to view report")
    print("Or, type none to quit") 
    print("\n")
    choice = input("What department would you like to go to today? ")

    if choice == "none":
        is_on = False 
    elif choice == "report":
        print("\n") 
        print("Select which department report you would like to view: ")
        print("Coffee Department, type 'coffee_report' ")
        print("Candy Department, type 'candy_report' ")
        print("Meat Department, type 'meat_report' ")
        print("Fruit Department, type 'fruit_report' ")
        print("Veggies Department, type 'veggies_report' ")
        print("Deli Bread Department, type 'deli_bread_report' ")
        print("Pasta Condiments Department, type 'pasta_condiments_report' ")
        print("Dry Goods Department, type 'dry_goods_report' ")
        print("Baby Pet Department, type 'baby_pet_department_report' ")
        print("Paper Goods Department, type 'paper_goods_report' ")
        print("Dairy Department, type 'dairy_report' ")
        print("Frozen Food Department, type 'frozen_food_report' ")
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
            print(f"Money = ${profit}")
            print("\n")

        if choice_report == "meat_report":
            print(f"Chicken: {resources_meat['chicken']} chickens available")
            print(f"Beef: {resources_meat['beef']} beef available")
            print(f"Steak: {resources_meat['steak']} steak available")
            print(f"Tenderloin: {resources_meat['tenderloin']} tenderloin available")
            print(f"Sirloin: {resources_meat['sirloin']} sirloin available")
            print(f"Flank: {resources_meat['flank']} flank available")
            print(f"Shrimp: {resources_meat['shrimp']} shrimp available")
            print(f"Crab: {resources_meat['crab']} crab available")
            print(f"Lobster: {resources_meat['lobster']} lobster available")
            print(f"Money = ${profit}")
            print("\n")

        if choice_report == "fruit_report":
            print(f"Green Apples: {resources_fruit['green apples']} green apples available")
            print(f"Oranges: {resources_fruit['oranges']} oranges available")
            print(f"Bananas: {resources_fruit['bananas']} bananas available")
            print(f"Red Apples: {resources_fruit['red apples']} red apples available")
            print(f"Apricots: {resources_fruit['apricots']} apricots available")
            print(f"Blueberries: {resources_fruit['blueberries']} blueberries available")
            print(f"Blackberries: {resources_fruit['blackberries']} blackberries available")
            print(f"Cherries: {resources_fruit['cherries']} cherries available")
            print(f"Cranberries: {resources_fruit['cranberries']} cranberries available")
            print(f"Gooseberries: {resources_fruit['gooseberries']} gooseberries available")
            print(f"Raspberries: {resources_fruit['raspberries']} raspberries available")
            print(f"Strawberries: {resources_fruit['strawberries']} strawberries available")
            print(f"Grapes: {resources_fruit['grapes']} grapes available")
            print(f"Peaches: {resources_fruit['peaches']} peaches available")
            print(f"Pinneaples: {resources_fruit['pinneaples']} pinneaples available")
            print(f"Pomegranates: {resources_fruit['pomegranates']} pomegranates available")
            print(f"Watermelons: {resources_fruit['watermelons']} watermelons available")
            print(f"Money = ${profit}")
            print("\n")

        if choice_report == "veggies_report":
            print(f"Tomatoes: {resources_veggies['tomatoes']} tomatoes available")
            print(f"Cabbages: {resources_veggies['cabbages']} cabbages available")
            print(f"Asparaguses: {resources_veggies['asparaguses']} asparaguses available")
            print(f"Artichokes: {resources_veggies['artichokes']} artichokes available")
            print(f"Arugulas: {resources_veggies['arugulas']} arugulas available")
            print(f"Spinach: {resources_veggies['spinach']} spinach available")
            print(f"Beets: {resources_veggies['beets']} beets available")
            print(f"Bok Choys: {resources_veggies['bok choys']} bok choys available")
            print(f"Green Beans: {resources_veggies['green beans']} green beans available")
            print(f"Broccolis: {resources_veggies['broccolis']} broccolis available")
            print(f"Brussel Sprouts: {resources_veggies['brussel sprouts']} brussel sprouts available")
            print(f"Carrots: {resources_veggies['carrots']} carrots available")
            print(f"Cauliflower: {resources_veggies['cauliflower']} cauliflower available")
            print(f"Celery: {resources_veggies['celery']} celery available")
            print(f"Cucumbers: {resources_veggies['cucumbers']} cucumbers available")
            print(f"Egg Plants: {resources_veggies['eggplants']} eggplants available")
            print(f"Soybeans: {resources_veggies['soybeans']} soybeans available")
            print(f"Lettuce: {resources_veggies['lettuce']} lettuce available")
            print(f"Onions: {resources_veggies['onions']} onions available")
            print(f"Green Peppers: {resources_veggies['green peppers']} green peppers available")
            print(f"Potatoes: {resources_veggies['potatoes']} potatoes available")
            print(f"Money = ${profit}")
            print("\n")

        if choice_report == "deli_bread_report":
            print(f"Pasta: {resources_deli_bread['pasta']} pasta available")
            print(f"Ravioli Angliolio: {resources_deli_bread['ravioli angiolio']} ravioli angiolio available")
            print(f"Chocolate Cake: {resources_deli_bread['chocolate cake']} chocolate cake available")
            print(f"Chicken Salad: {resources_deli_bread['chicken salad']} chicken salad available")
            print(f"Egg Salad: {resources_deli_bread['egg salad']} egg salad available")
            print(f"Tuna: {resources_deli_bread['tuna']} tuna available")
            print(f"Turkey: {resources_deli_bread['turkey']} turkey available")
            print(f"Money = ${profit}")
            print("\n")

        if choice_report == "pasta_condiments_report":
            print(f"White Wine: {resources_pasta_condiments['white wine']} white wine available")
            print(f"Parmesan Cheese: {resources_pasta_condiments['parmesan cheese']} parmesan cheese available")
            print(f"Butter: {resources_pasta_condiments['butter']} butter available")
            print(f"Thousand Island Sauce: {resources_pasta_condiments['thousand island sauce']} thousand island sauce available")
            print(f"Ketchup: {resources_pasta_condiments['ketchup']} ketchup available")
            print(f"Mustard: {resources_pasta_condiments['mustard']} mustard available")
            print(f"Teriyaki Sauce: {resources_pasta_condiments['teriyaki sauce']} teriyaki sauce available")
            print(f"Money = ${profit}")
            print("\n")

        if choice_report == "dry_goods_report":
            print(f"Cereal: {resources_dry_goods['cereal']} cereal available")
            print(f"Hummus: {resources_dry_goods['hummus']} hummus available")
            print(f"Peanut Butter: {resources_dry_goods['peanut butter']} peanut butter available")
            print(f"Eggs: {resources_dry_goods['eggs']} eggs available")
            print(f"Frozen Fruit: {resources_dry_goods['frozen fruit']} frozen fruit available")
            print(f"Tofu: {resources_dry_goods['tofu']} tofu available")
            print(f"Granola Bars: {resources_dry_goods['granola bars']} granola bars available")
            print(f"Salmon: {resources_dry_goods['salmon']} salmon available")
            print(f"Chickpeas: {resources_dry_goods['chickpeas']} chickpeas available")
            print(f"Beef Jerky: {resources_dry_goods['beef jerky']} beef jerky available")
            print(f"Canned Fruit: {resources_dry_goods['canned fruit']} canned fruit available")
            print(f"Macaroni and Cheese: {resources_dry_goods['macaroni and cheese']} macaroni and cheese available")
            print(f"Money = ${profit}")
            print("\n")

        if choice_report == "baby_pet_department_report":
            print(f"Stuffed Animals: {resources_baby_pet_department['stuffed animals']} stuffed animals available")
            print(f"Baby Bath: {resources_baby_pet_department['baby bath']} baby baths available")
            print(f"Baby Food Maker: {resources_baby_pet_department['baby food maker']} baby food makers available")
            print(f"Breast-Feeding Bottle: {resources_baby_pet_department['breast-feeding bottle']} breast-feeding bottles available")
            print(f"Strollers: {resources_baby_pet_department['strollers']} strollers available")
            print(f"Diaper Bags: {resources_baby_pet_department['diaper bags']} diaper bags available")
            print(f"Portable Cribs: {resources_baby_pet_department['portable cribs']} portable cribs available")
            print(f"Bath Towels: {resources_baby_pet_department['bath towels']} bath towels available")
            print(f"Pacifiers: {resources_baby_pet_department['pacifiers']} pacifiers available")
            print(f"Food Bags: {resources_baby_pet_department['food bags']} food bags available")
            print(f"Potty Trainers: {resources_baby_pet_department['potty trainers']} potty trainers available")
            print(f"Baby Healing Ointments: {resources_baby_pet_department['baby healing ointments']} baby healing ointments available")
            print(f"Thermometers: {resources_baby_pet_department['thermometers']} thermometers available")
            print(f"Baby Toys: {resources_baby_pet_department['baby toys']} baby toys available")
            print(f"Baby Wipes: {resources_baby_pet_department['baby wipes']} baby wipes available")
            print(f"Vitamin A Pills: {resources_baby_pet_department['vitamin A pills']} vitamin A pills available")
            print(f"Vitamin B Pills: {resources_baby_pet_department['vitamin B pills']} vitamin B pills available")
            print(f"Vitamin C Pills: {resources_baby_pet_department['vitamin C pills']} vitamin C pills available")
            print(f"Vitamin D Pills: {resources_baby_pet_department['vitamin D pills']} vitamin D pills available")
            print(f"Car Seats: {resources_baby_pet_department['car seats']} car seats available")
            print(f"Sunscreen: {resources_baby_pet_department['sunscreen']} sunscreen available")
            print(f"Money = ${profit}")
            print("\n")

        if choice_report == "paper_goods_report":
            print(f"Writing Paper Pads: {resources_paper_goods['writing paper pad']} writing paper pads available")
            print(f"Letter Papers: {resources_paper_goods['letter papers']} letter papers available")
            print(f"Note-Card Sets: {resources_paper_goods['note-card set']} note-card sets available")
            print(f"Assorted Postcards: {resources_paper_goods['assorted postcards']} assorted postcards available")
            print(f"Notecards: {resources_paper_goods['notecards']} notecards available")
            print(f"Cable Management Boxes: {resources_paper_goods['cable management boxes']} cable management boxes available")
            print(f"Sticky Notes: {resources_paper_goods['sticky notes']} sticky notes available")
            print(f"File Organizers: {resources_paper_goods['file organizers']} file organizers available")
            print(f"Money = ${profit}")
            print("\n")

        if choice_report == "dairy_department_report":
            print(f"Cheddar Snack Cheese: {resources_dairy_department['cheddar snack cheese']} cheddar snack cheese available")
            print(f"Mozzarella String Cheese: {resources_dairy_department['mozzarella string cheese']} mozzarella string cheese available")
            print(f"Swiss Premium Cheese Slices: {resources_dairy_department['swiss premium cheese slices']} swiss premium cheese slices available")
            print(f"Cottage Cheese: {resources_dairy_department['cottage cheese']} cottage cheese available")
            print(f"Cream Cheese: {resources_dairy_department['cream cheese']} cream cheese available")
            print(f"Peeled Eggs: {resources_dairy_department['peeled eggs']} peeled eggs available")
            print(f"Lowfat 1% Milk: {resources_dairy_department['lowfat 1% milk']} lowfat 1% milk available")
            print(f"Coconut Milk: {resources_dairy_department['coconut milk']} coconut milk available")
            print(f"Almond Milk: {resources_dairy_department['almond milk']} almond milk available")
            print(f"Greek Yogurt: {resources_dairy_department['greek yogurt']} greek yogurt available")
            print(f"Plain Yogurt: {resources_dairy_department['plain yogurt']} plain yogurt available")
            print(f"Money = ${profit}")
            print("\n")

        if choice_report == "frozen_report":
            print(f"Chicken Tikka Masala: {resources_frozen_food['chicken tikka masala']} chicken tikka masalas available")
            print(f"Mac And Cheese: {resources_frozen_food['mac and cheese']} mac and cheese available")
            print(f"Orange Chicken: {resources_frozen_food['orange chicken']} orange chicken available")
            print(f"Ravioli: {resources_frozen_food['ravioli']} ravioli available")
            print(f"Ravioli Bowls: {resources_frozen_food['ravioli bowls']} ravioli bowls available")
            print(f"Corn Enchiladas: {resources_frozen_food['corn enchiladas']} corn enchiladas available")
            print(f"Casserole Bowls: {resources_frozen_food['casserole bowls']} casserole bowls available")
            print(f"Stuffed Peppers: {resources_frozen_food['stuffed peppers']} stuffed peppers available")
            print(f"Enchiladas: {resources_frozen_food['enchiladas']} enchiladas available")
            print(f"Lasagna: {resources_frozen_food['lasagna']} lasagna available")
            print(f"Chicken Pot Pie: {resources_frozen_food['chicken pot pie']} chicken pot pie available")
            print(f"Burritos: {resources_frozen_food['burritos']} burritos available")
            print(f"Waffles: {resources_frozen_food['waffles']} waffles available")
            print(f"Egg White Scramble: {resources_frozen_food['egg white scramble']} egg white scramble available")
            print(f"Cheese Pizza: {resources_frozen_food['cheese pizza']} cheese pizza available")
            print(f"Salmon Burgers: {resources_frozen_food['salmon burgers']} salmon burgers available")
            print(f"Falafel Wrap: {resources_frozen_food['falafel wrap']} falafel wraps available")
            print(f"Money = ${profit}")
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

    if choice == "3":
        print("\n")
        print("Available options: ")
        print("Chicken")
        print("Beef") 
        print("Steak")
        print("Tenderloin")
        print("Sirloin")
        print("Flank")
        print("Shrimp")
        print("Crab")
        print("Lobster")
        print("\n")
        choice_meat = input("What would you like to go to buy today? ")

        meat = MEAT_MENU[choice_meat]
        if is_resource_sufficient_meat(meat["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, meat["cost"]):
                make_meat(choice_meat, meat["ingredients"])  

        check_keep_going = input("Would you like to keep going? Type 'Y' or 'N': ")
        check_keep_going = check_keep_going.lower()
        if check_keep_going == 'y':
            is_on = True
        else:
            is_on = False

