import random
from turtle import Turtle

AVAILABLE_COLORS = [
    (255, 89, 94),
    (255, 202, 58),
    (138, 201, 38),
    (25, 130, 196),
    (106, 76, 147)
]


class Stone(Turtle):

    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.shapesize(1, 3)
        self.penup()
        self.speed(1000)
        self.setx(pos_x)
        self.sety(pos_y)
        self.fillcolor(random.choice(AVAILABLE_COLORS))
        self.showturtle()
        self.status = 1

    def delete_stone(self):
        self.status = 0
        self.hideturtle()
