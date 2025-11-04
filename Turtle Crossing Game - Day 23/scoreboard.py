from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(-290,250)
        self.update_scoreboard()

    # erase the last scoreboard and write again a new one with the correct score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="left", font=FONT)

    # Increase 1 point to the scoreboard
    def score_points(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.home() #go to x= 0,y= 0 position
        self.write("GAME OVER", move=False, align="center", font=FONT)