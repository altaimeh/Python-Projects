from distutils.fancy_getopt import wrap_text
from readline import read_init_file
from textwrap import wrap
import textwrap
from turtle import Turtle, Screen, bgcolor
from tkinter import *

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
    screen = Screen()
    screen.exitonclick()

def wipe_text():
    write.delete('1.0', END)


def stop_writing(event):
    global stop_writing_id
    disappear.after_cancel(stop_writing_id)  
    stop_writing_id = disappear.after(1000, wipe_text) 

game_quit_value = False
print("\n")
print("Please pick from the following games to play from ")
print("\n")
print("Choices: ")
print("1) To let the computer draw a string for you, type 1")
print("2) To draw a string yourself and have it disappear in a few seconds, type 2")
input_game_choice = int(input("Choice: "))
while game_quit_value:
    if input_game_choice == 1:
        play_game()
        
    else:
        game_quit_value = True

if input_game_choice == 1:
    play_game()
if input_game_choice == 2:

    disappear = Tk()
    disappear.resizable(width=False, height=False)
    disappear.config(bg="black")
    disappear.title("Disappearing text App")

    stop_writing_id = 'after'
    disappear_text = Label(disappear, text="Start typing and text will disappear after a few seconds...", fg="red", font=("Helvetica", 18), pady=20, padx=20, bg="black")
    disappear_text.grid(row=0, column=0)
    write = Text(disappear, wrap=WORD, relief=FLAT, padx=14, pady=15, fg="red", font=("Helvetica", 14))
    write.grid(row=1, column=0)
    write.configure({"background": "black"})
    write.focus()
    write.bind('<KeyRelease>', stop_writing)
    disappear.mainloop()

print("Thanks for playing! ")
print("\n" * 2)
