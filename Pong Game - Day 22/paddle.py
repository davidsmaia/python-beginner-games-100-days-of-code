# TODO 2 Create a white Paddle on the right side of the screen
# width = 20, height = 100 x_pos = 350, y_pos = 0
# move it up and down

from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, starting_position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1) #20x20 is the default size
        self.setposition(x=starting_position[0], y=starting_position[1])

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)