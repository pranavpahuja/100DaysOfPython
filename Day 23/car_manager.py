import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    # pass
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(0)
        self.shapesize(stretch_wid=0.5, stretch_len=2)

    def spawn_cars(self):
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(0, 0)