import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car=CarManager()
board=Scoreboard()

screen.listen()
screen.onkey(player.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    for c in car.all_cars:
        if c.distance(player)<20:
            board.finito()
            game_is_on=False

    if player.ycor()>=280:
        player.finish()
        car.levelup()
        board.lvlup()





screen.exitonclick()
