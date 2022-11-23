import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=500)
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")
screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #Detect Collisions with wall
    if ball.ycor() > 230 or ball.ycor() < -230:
        #Needs to bounce
        ball.bounce_y()

    #Detect Collisions with the paddle
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    #Detect paddle misses the the ball
    if ball.xcor() > 380:
        ball.resetpos()
        scoreboard.lpoint()
        ball.xmove = 12
        ball.ymove = 10

    if ball.xcor() < -380:
        ball.resetpos()
        scoreboard.rpoint()
        ball.xmove = 12
        ball.ymove = 10


screen.exitonclick()
