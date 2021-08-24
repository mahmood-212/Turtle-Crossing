from turtle import Turtle
FONT= ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score= 0
        self.penup()
        self.color("black")
        self.goto(-250, 250)
        self.write(f"level: {self.score} ", align="left", font=FONT)

    def add_score(self):
        self.score += 1

    def level_board(self):
        self.write(f"level: {self.score} ", align="left", font=FONT)
