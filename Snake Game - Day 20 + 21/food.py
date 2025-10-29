from turtle import Turtle
import random


# TODO Make the food class inherit from Turtle class

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh() # -> method created below to generate the food in a random location
        # random_x = random.randint(-280,280)
        # random_y = random.randint(-280,280)
        # self.goto(random_x, random_y)

    # Method to generate the food in a random location.
    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x, random_y)