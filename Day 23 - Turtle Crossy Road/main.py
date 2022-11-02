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
    # car_manager.create_cars()
    car_manager.motion(scoreboard.score)
    car_manager.create_car()

    if player.ycor() > 280:
        player.resetpos()
        scoreboard.increase_score()
        scoreboard.refresh()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.end_game()
            game_is_on = False

screen.exitonclick()