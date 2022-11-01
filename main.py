import time
from turtle import *
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from stone import Stone

LIMIT_LEFT = -250  # Screen limit left
LIMIT_RIGHT = 250  # Screen limit right
ROWS = 5  # Number of stone rows
COLUMNS = 7  # Number of stone columns
INIT_X = -200  # Initial 'x' position of the first stone
INIT_Y = 200  # Initial 'y' position of the first stone
SPACING_X = 65  # Spacing 'x' between the center of the stones
SPACING_Y = 25  # Spacing 'y' between the center of the stones

# Screen definition
setup(500, 500)
screen = Screen()
screen.colormode(255)
screen.tracer(0)
screen.bgcolor('black')
screen.listen()

# Stones definition
stones = []
for row in range(ROWS):
    for col in range(COLUMNS):
        pos_x = INIT_X + col * SPACING_X
        pos_y = INIT_Y - row * SPACING_Y
        stone = Stone(pos_x, pos_y)
        stones.append(stone)

# Player definition
paddle = Paddle(LIMIT_LEFT, LIMIT_RIGHT)
screen.onkey(paddle.move_left, 'Left')
screen.onkey(paddle.move_right, 'Right')

# Ball definition
ball = Ball()
ball.goto(0, 0)

# Scoreboard definition
scoreboard = Scoreboard()

game_is_on = True
active_stones = [stone for stone in stones if stone.status == 1]
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 225:
        # Needs to bounce
        ball.bounce_y()

    if ball.xcor() > 225 or ball.xcor() < -225:
        # Needs to bounce
        ball.bounce_x()

    # Detect collision with paddle
    if ball.ycor() <= paddle.ycor() + 20 and \
            paddle.xcor() + 50 > ball.xcor() > paddle.xcor() - 50:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with stones
    for active_stone in active_stones:
        if active_stone.ycor() + 25 > ball.ycor() > active_stone.ycor() - 25 and \
                active_stone.xcor() + 30 > ball.xcor() > active_stone.xcor() - 30:
            # Needs to bounce and point is added
            ball.bounce_y()
            ball.increase_speed()
            active_stone.delete_stone()
            active_stones = [stone for stone in stones if stone.status == 1]
            scoreboard.point()
            break

    # Check if ball exited board
    if ball.ycor() < -225:
        game_is_on = False
        # Game over
        scoreboard.finish_message("Game Over!")

    # Check if no more stones are left
    if len(active_stones) == 0:
        game_is_on = False
        # Won game
        scoreboard.finish_message("Congratulations!")

    screen.update()

screen.exitonclick()
