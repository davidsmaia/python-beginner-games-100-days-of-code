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
        with open('data.txt', 'r') as data:# Takes the value from the data file
            self.high_score = int(data.read()) #Saving the data in a variable after transforming it to INT

        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",move=False,align=ALIGNMENT,font=FONT)


    # Update the scoreboard on the screen
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}",move=False,align=ALIGNMENT,font=FONT)

    # Add 1 to the score
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    # Update the high_score and reset the score counter
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.high_score)) #writes the new high score and saves it
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(arg=f"GAME OVER",move=False,align=ALIGNMENT,font=FONT)

