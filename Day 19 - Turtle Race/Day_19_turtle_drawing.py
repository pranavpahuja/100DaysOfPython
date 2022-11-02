from turtle import *

tim = Turtle()

screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_left():
    tim.speed("fastest")
    x=tim.heading()
    tim.setheading(x+10)

def move_right():
    tim.speed("fastest")
    y=tim.heading()
    tim.setheading(y-10)

def clear():

    tim.penup()
    tim.goto(0,0)
    tim.clear()
    tim.pendown()

screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()