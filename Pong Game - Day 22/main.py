# TODO 1 Create a black screen with 600 height and 800 width
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# Creating the screen
screen = Screen()
screen.setup(width=800, height=600) #size
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen() #Listen the key that's been pressed -> allows the movements
screen.tracer(0) #disable the animation. It requires a refresh of the screen -> Used to not show Paddles going to its position


# Creating the Paddle
# TODO 3 create a second paddle on the Left side using POO
r_paddle = Paddle((350,0)) #moves with 'Up' and 'Down' arrows
l_paddle = Paddle((-350,0)) #moves with 'w' and 's' keys
ball = Ball()
scoreboard = Scoreboard()

# Detecting the Paddle moves -> Right side, Arrow keys
screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
# Detecting the Paddle moves -> Left side,'w' and 's' keys
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")


game_is_on = True
while game_is_on:
    # TODO 7 Increase the speed when the ball hits the paddle to make the game difficult by the time
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO 5 Detect collision with top and bottom walls and Change the ball movement direction
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.change_y_direction()

    # Detect collision with paddles
        # the distance between the ball the paddle should be less than 50 not 20 because it's measure from the center of the paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.change_x_direction()


    # TODO 6 Detect if the ball goes out of bounds at the edge of the screen.
    # If yes, reset the ball's position to the center of the screen
    # The ball should then start moving towards the other player
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    # Detect if left paddle misses
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick() #holds the screen opened until the player clicks to close it
