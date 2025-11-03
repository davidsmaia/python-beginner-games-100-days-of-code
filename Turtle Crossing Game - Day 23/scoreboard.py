from turtle import Turtle

from pandas.io.formats.info import frame_see_also_sub

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(-290,250)
        self.write(f"Score: {self.score}", move=False, align="left", font=FONT)

    # Increase 1 point to the scoreboard
    def score_points(self):
        self.score += 1
        self.clear() # erase the last scoreboard and write again a new one with the correct score
        self.write(f"Score: {self.score}", move=False, align="left", font=FONT)
