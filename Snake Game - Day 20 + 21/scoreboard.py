# TODO Create a new Scoreboard Class. It must be inherited from Turtle Class

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial",20,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.setposition(x=0, y=270)
        self.score = 0
        self.write(arg=f"Score: {self.score}",move=False,align=ALIGNMENT,font=FONT)

    # Add 1 to the score
    def increase_score(self):
        self.score += 1
        self.clear() #clears the previous score to write the new one
        self.write(arg=f"Score: {self.score}",move=False,align=ALIGNMENT,font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"GAME OVER",move=False,align=ALIGNMENT,font=FONT)

