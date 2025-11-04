from turtle import Turtle

FONT = ("Courier", 24, "normal")

class RoadLine(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("yellow")
        self.upper_lines()
        self.lower_lines()

    def upper_lines(self):
        self.setposition(0,10)
        self.write("- " * 18, move=False, align="center",font=FONT)

    def lower_lines(self):
        self.setposition(0, -10)
        self.write("- " * 18, move=False, align="center", font=FONT)

