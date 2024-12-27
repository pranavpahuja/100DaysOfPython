import random
from turtle import Turtle

SCORE_IS = 0
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        global SCORE_IS
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def increase_score(self):
        global SCORE_IS
        SCORE_IS += 1

    def refresh(self):
        global SCORE_IS
        self.clear()
        self.write("Score is: {}".format(SCORE_IS), font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", font=FONT, align=ALIGNMENT)