import random
import time

from turtle import Screen, Turtle
from Snake import Snake


screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

segments = []

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

screen.exitonclick()