COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


from turtle import Turtle
import random

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.carspeed=STARTING_MOVE_DISTANCE
    def create_car(self):
        dice=random.randint(1,6)
        if dice==2:
            new_car =Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            startingpos=random.choice(range(-250,+250))
            new_car.goto(320,startingpos)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.carspeed)
    def levelup(self):
        self.carspeed+=MOVE_INCREMENT



