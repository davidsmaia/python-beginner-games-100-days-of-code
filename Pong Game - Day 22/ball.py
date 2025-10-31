# TODO 4 Create a Ball Class that generates a ball at the center of the screen
# Width = 20, Height = 20. Should move to northeast direction, to the top right edge of the screen

from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.shape("circle")
        # self.setposition(0,0) #unnecessary, all turtles objects starts at 0,0
        self.y_direction = 10
        self.x_direction = 10
        self.move_speed = 0.1

    def move(self):
        pos = self.position() # (X, Y) coordinates
        self.goto(pos[0] + self.x_direction, pos[1] + self.y_direction)

    def change_y_direction(self):
        self.y_direction *= -1

    def change_x_direction(self):
        self.x_direction *= -1
        self.move_speed *= 0.9

    def restart(self):
        self.home()
        self.move_speed = 0.1
        self.change_x_direction()
