import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road_line import RoadLine

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.tracer(0)

road_line = RoadLine()
player = Player() # creating the player's turtle object
car_manager = CarManager() #creating the car object
scoreboard = Scoreboard() # creating the scoreboard object

screen.listen() # get the key pressed by the player
screen.onkeypress(fun=player.move_forwards, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars() #create a new car every refresh of the loop
    car_manager.move_cars()

    # Detecting collision with a car
    for car in car_manager.all_cars: #checking every car object
        if car.distance(player) < 20:
            game_is_on = False # Game over
            scoreboard.game_over()

    # Detecting that the Player get to the other side and speeding the cars velocity
    if player.ycor() > 280:
        scoreboard.score_points() # Increase a point to the scoreboard
        player.reset_position() # Get the player to the initial position once again
        car_manager.leve_up() #incresing the cars speed by 10 each time the player makes a point

screen.exitonclick()