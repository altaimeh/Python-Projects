from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#intro
print("\n")
print("Hello! Welcome to the snake game")
background_color_input = input("What color would your like your background to be? (no red or yellow please): ")
game_name = input("What would you like the name of your game to be?: ")
#set screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(background_color_input)
screen.title(game_name)
screen.tracer(0)
#create objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()
#set screen listener for controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
#loop through until is over
while game_is_on:
    #update screen
    screen.update()
    #set move speed to 0.1 to allow simultaneous movement
    time.sleep(0.1)
    #call snake's move function
    snake.move()
    #if the body is near food, refresh the food to a new random location and extend the body and increase score
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    #if body is about to hit border, end game
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        game_is_on = False
        scoreboard.game_over()
    #if the head is about to hit the body, then game over
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

print("\n")
print("Thanks for playing!")
print("\n")
screen.exitonclick()



    