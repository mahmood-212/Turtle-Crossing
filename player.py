from turtle import Turtle

STARTING_POSITION=(0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move_player(self):
        self.forward(MOVE_DISTANCE)

    def move_back(self):
        self.backward(MOVE_DISTANCE)

    def starting_position(self):
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.write(f"Game Over", align="center", font=("Courier", 24, "normal"))