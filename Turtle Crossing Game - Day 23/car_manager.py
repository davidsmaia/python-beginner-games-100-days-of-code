from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green","blue", "purple", "pink", "black", "white"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.cars_position = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # Creates both upper and lower cars
    def create_cars(self):
        # reducing the amount of cars being created by using a random chance
        random_chance = random.randint(1, 12)
        if random_chance == 1:
            self.create_lower_car()
            self.create_upper_car()

    # Car settings, such as shape, size, color.
    def car_settings(self, heading):
        car = Turtle("square")
        car.shapesize(1,2) #20px high and 40px wide
        car.penup()
        car.color(random.choice(COLORS))
        car.setheading(heading) #heading must be inserted as an input on each car generator
        return car

    # Generates the lower cars, moving it from left to right
    def create_lower_car(self):
        #cars settings
        new_lower_car = self.car_settings(180) #heading to left <-
        new_lower_car.setx(random.randint(300, 400))
        new_lower_car.sety(random.randint(-250, -10))
        self.all_cars.append(new_lower_car)


    # Generates the upper cars, moving it from right to left
    def create_upper_car(self):
        #cars settings
        new_upper_car = self.car_settings(0)  # heading to left ->
        new_upper_car.setx(random.randint(a=-400, b=-300))
        new_upper_car.sety(random.randint(50, 250))
        self.all_cars.append(new_upper_car)

    # moving all the cars in the list "all_cars []"
    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    # Increasing the cars speed by 10
    def leve_up(self):
        self.car_speed += MOVE_INCREMENT

