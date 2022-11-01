from turtle import Screen
from Paddles import Paddles
import time
from Ball import Ball
from Scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

r_paddle = Paddles((350, 0))
l_paddle = Paddles((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #collision
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddlebounce()

    if ball.xcor() > 380:
        ball.reset_position()
        ball.paddlebounce()
        scoreboard.l_score += 1
        scoreboard.refresh()
        scoreboard.score()
        time.sleep(0.5)

    if ball.xcor() < -380:
        ball.reset_position()
        ball.paddlebounce()
        scoreboard.r_score += 1
        scoreboard.refresh()
        scoreboard.score()
        time.sleep(0.5)

screen.exitonclick()