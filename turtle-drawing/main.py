from turtle import Turtle, Screen, bgcolor

quit_value = True
def play_game():
    print("\n")
    print("Welcome to LetsDraw")
    name = input("Name: ")
    print(f"Hi There: {name} ")
    string_input = input("Type a string that you would like to draw: ")
    background_input = input("What color would you like the background color to be?: ")
    color_input = input("What color would you like the text color?: ")
    print("\n")
    turtle_avatar = Turtle() 
    bgcolor(background_input)
    turtle_avatar.color(color_input)
    style = ('Courier', 45, 'normal')
    turtle_avatar.write(string_input, font=style, align='center')
    turtle_avatar.hideturtle()
    
while input("Do you want to play a game of LetsDraw? Type 'y' or 'n': ") == "y":
    play_game()
    screen = Screen()
    screen.exitonclick()

print("Thanks for playing! ")
print("\n" * 2)
