from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.cars_position = []

    def create_car(self):
        # reducing the amount of cars being created by using a random chance
        random_chance = random.randint(1,6)
        if random_chance == 1:
            #cars settings
            new_car = Turtle("square")
            new_car.shapesize(1,2) #20px high and 40px wide
            new_car.penup()
            new_car.setheading(180) #heading to left <-
            new_car.color(random.choice(COLORS))
            new_car.setx(random.randint(300, 400))
            new_car.sety(random.randint(-250, 250))
            self.all_cars.append(new_car)


    # moving all the cars in the list "all_cars []" to the left
    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)