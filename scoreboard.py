from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def point(self) -> None:
        """
        Adds point to score
        """
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        """
        Rewrites scoreboard string with updated score
        """
        self.clear()
        self.goto(-225, 215)
        message = f"Score: {self.score}"
        self.write(message, align="left", font=("Arial", 18, "bold"))

    def finish_message(self, message) -> None:
        """
        Writes the final message of the game in the center of the board
        """
        self.goto(0, 0)
        self.write(message, align='center', font=("Arial", 30, "bold"))