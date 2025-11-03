import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player() # creating the player's turtle object
car_manager = CarManager() #creating the car object
scoreboard = Scoreboard()

screen.listen() # get the key pressed by the player
screen.onkeypress(fun=player.move_forwards, key="Up")

loop_counter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car() #create a new car every refresh of the loop
    car_manager.move_cars()

    # Detecting collision with a car
    for car in car_manager.all_cars: #checking every car object
        if car.distance(player) < 20:
            game_is_on = False # Game over

    # Detecting that the Player get to the other side and speeding the cars velocity
    if player.ycor() > 280:
        scoreboard.score_points() # Increase a poin to the scoreboard
        player.reset_position() # Get the player to the initial position once again

        # TODO Increase the cars velocity

screen.exitonclick()