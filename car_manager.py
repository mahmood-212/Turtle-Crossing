from turtle import Turtle
import random

COLORS = ["red", "blue", "green", "orange", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.all_cars = []
        self.speed_car = STARTING_MOVE_DISTANCE

    def made_cars(self):
        random_car = random.randint(1, 6)
        if random_car == 1:
            cars_2 = Turtle("square")
            cars_2.shapesize(stretch_wid=1, stretch_len=2)
            cars_2.penup()
            cars_2.goto(x=300, y=random.randint(-250, 250))
            cars_2.color(random.choice(COLORS))
            self.all_cars.append(cars_2)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.speed_car)

    def increment_speed(self):
        self.speed_car += MOVE_INCREMENT
