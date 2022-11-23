from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.Lscore = 0
        self.Rscore = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 175)
        self.write(self.Lscore, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 175)
        self.write(self.Rscore, align="center", font=("Courier", 50, "normal"))

    def lpoint(self):
        self.Lscore += 1
        self.update_scoreboard()

    def rpoint(self):
        self.Rscore += 1
        self.update_scoreboard()
