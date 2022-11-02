import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")
# screen.onkey(player.go_down, "Down")
i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    i += 1
    car_manager.motion(scoreboard.score)

    if player.ycor() > 280:
        player.resetpos()
        scoreboard.increase_score()
        scoreboard.refresh()

    if i == 6:
        i = 0
        car_manager.spawn_cars()

    # for car in cars:
    #     if car.distance(player) < 10:
    #         game_is_on = False