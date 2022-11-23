from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    def down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy)


