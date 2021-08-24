from turtle import Turtle, Screen
from car_manager import CarManager
from score_board import Scoreboard
from player import Player
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
tom = Player()
cars = CarManager()
score_board = Scoreboard()

screen.onkeypress(key="Up", fun=tom.move_player)
screen.onkeypress(key="Down", fun=tom.move_back)

# all_car = []

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    cars.made_cars()
    cars.move_car()
    score_board.level_board()

    for i in cars.all_cars:
        if i.distance(tom) < 20:
            is_game_on = False
            tom.game_over()

    if tom.ycor() > 250:
        score_board.add_score()
        tom.starting_position()
        cars.increment_speed()
        score_board.clear()
        score_board.level_board()
        tom.move_player()






