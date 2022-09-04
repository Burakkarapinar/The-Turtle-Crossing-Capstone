FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0, 265)
        self.write(f"Level: {self.level}", align="center", font=(FONT))
    def lvlup(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=(FONT))
    def finito(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=(FONT))