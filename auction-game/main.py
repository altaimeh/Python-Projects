from art import phone
from art import AirPods
from art import TV


bids = {}

bidding_finished = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder 
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while bidding_finished:

    name = input("What is your name?: ")
    print("What would you like to buy?")
    print("Available options: ")
    print("1) Phone, Type '1'")
    print("2) AirPods, Type '2'")
    print("3) TV, Type '3'")
    buy_option = int(input("What is your option?: "))
    if buy_option == 1:
        print(phone)
        price = int(input("What is your bid?: $"))

        bids[name] = price

        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if should_continue == "no":
            bidding_finished = False 
            find_highest_bidder(bids)

        elif should_continue == "yes":
            print("\n" * 50)
            print(phone)

    if buy_option == 2:
        print(AirPods)
        price = int(input("What is your bid?: $"))

        bids[name] = price

        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if should_continue == "no":
            bidding_finished = False 
            find_highest_bidder(bids)

        elif should_continue == "yes":
            print("\n" * 50)
            print(phone)

    if buy_option == 3:
        print(TV)
        price = int(input("What is your bid?: $"))

        bids[name] = price

        should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
        if should_continue == "no":
            bidding_finished = False 
            find_highest_bidder(bids)

        elif should_continue == "yes":
            print("\n" * 50)
            print(phone) 

    

