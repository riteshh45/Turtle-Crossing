COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager():
    def __init__(self):
        self.all_cars=[]
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance=random.randint(1,8)
        if random_chance==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(COLORS[random.randint(0, 5)])
            y_cor = random.randint(-250, 250)
            new_car.goto(280, y_cor)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed+=MOVE_INCREMENT







