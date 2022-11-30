import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Turtle Crossing Capstone")
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.running()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    if player.finish():
        scoreboard.increase_score()
        player.reset_position()
        car_manager.levelup()

screen.exitonclick()