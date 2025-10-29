from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black") #screen color
screen.title("My Snake Game")
screen.tracer(0)

# creating a snake object
snake = Snake()

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

screen.exitonclick() # hold the screen until we click to close
