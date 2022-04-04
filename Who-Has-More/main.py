from art import logo, vs
from game_data import data
import random


def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    print(f"{account_name}, is a {account_descr}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess ==  "a"
    else:
        return guess == "b" 

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)
    

    while account_a == account_b:
        account_b  = random.choice(data)

    print(f"Compare: {format_data(account_a)}")
    print(vs)
    print(f"Compare: {format_data(account_b)}")


    guess = input("Who has more followers? Type 'A' or 'B': ")
    guess = guess.lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]


    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print("\n")
        print(f"Yay! you got it right: current score: {score}")
        print("\n")
    else:
        game_should_continue = False
        print("\n")
        print(f"Sorry, that's incorrect. Final Score: {score}")
        print("\n")
            


