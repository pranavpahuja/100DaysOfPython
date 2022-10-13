import random

from turtle import Screen, Turtle

snake = Turtle()

def spawnFood():
    x_pos = random.randint()

def snake_setup():
    snake.penup()
    snake.shape("circle")
    snake.pensize(width=5)
    snake.color("white")
    snake.fillcolor("white")
    snake.home()
    snake.pendown()

def move_up():
    snake.heading(90)
    snake.forward(500)

snake_setup()
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.onkey(move_up, key="w")

screen.exitonclick()