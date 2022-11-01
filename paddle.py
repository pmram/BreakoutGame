from turtle import Turtle

INCREMENT = 30


class Paddle(Turtle):

    def __init__(self, window_limit_left, window_limit_right):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 5.5)
        self.color('white')
        self.penup()
        self.sety(-220)
        self.limit_left = window_limit_left
        self.limit_right = window_limit_right

    def move_left(self):
        if self.xcor() > self.limit_left + 80:
            self.goto(self.xcor() - INCREMENT, self.ycor())

    def move_right(self):
        if self.xcor() < self.limit_right - 80:
            self.goto(self.xcor() + INCREMENT, self.ycor())
