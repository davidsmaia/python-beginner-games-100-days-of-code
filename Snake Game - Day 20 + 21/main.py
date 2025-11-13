from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") #screen color
screen.title("My Snake Game")
screen.tracer(0)

# creating a snake object
snake = Snake()
food = Food()
scoreboard = Scoreboard() #creating the scoreboard object


screen.listen() #start listen the keystrokes

# Functionalities to move the snake
screen.onkey(fun=snake.up,key="Up") #Up arrow key, must move to north
screen.onkey(fun=snake.down, key="Down") #Down arrow key, must move to south
screen.onkey(fun=snake.left, key="Left") #Left arrow key, must move to West
screen.onkey(fun=snake.right, key="Right") #Right arrow key, must move to East

# While loop to maintain tha game on
game_is_on = True
while game_is_on:
    screen.update() #refreshes the screen after 0.1 second
    time.sleep(0.1) #delay the refresh
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15: #checks the distance between the snake head and the food (the food is 10x10)
        # print("nhami nhami nhami")
        food.refresh()
        snake.extend() #increase a new segment on the snake
        scoreboard.increase_score() #add 1 to the score

    # Detect collisions with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collisions with its own tail
    for segment in snake.segments[1:]: #skips the very first segment because it's the head...

        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick() # hold the screen until we click to close
