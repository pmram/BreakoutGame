from turtle import Turtle

INCREMENT = 1  # Sets up the increment in distance for each iteration


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color('white')
        self.goto(0, 0)
        self.x_move = INCREMENT
        self.y_move = INCREMENT
        self.move_speed = 0.001

    def move(self):
        """
        Moves the ball in a defined INCREMENT
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """
        Alternates the sign of 'x' axis movement
        """
        self.x_move *= -1

    def bounce_y(self):
        """
        Alternates the sign of 'y' axis movement
        """
        self.y_move *= -1

    def reset_position(self):
        """
        Resets the ball to the center of the board
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def increase_speed(self) -> None:
        """
        Increases the speed of ball movement
        """
        self.move_speed *= 0.90
