from turtle import Turtle
import time


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-280, 280)
        self.score_value()

    def refresh(self):
        self.clear()
        self.goto(-295, 280)
        self.write("Level: {}".format(self.score), align="left", font=("Courier", 20, "normal"))

    def score_value(self):
        self.goto(-295, 280)
        self.write("Level: {}".format(self.score), align="left", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score += 1
