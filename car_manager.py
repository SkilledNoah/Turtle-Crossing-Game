from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "white"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.move_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(choice(COLORS))
        new_car.penup()
        new_car.shapesize(1, 2)
        random_y = randint(-240 // 20, 220 // 20) * 20
        if random_y >= -10:
            new_car.goto(-280, random_y)
        else:
            new_car.goto(280, random_y)
        self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            if car.ycor() >= -10:
                car.forward(self.move_speed)
            else:
                car.backward(self.move_speed)

    def increase_difficulty(self):
        self.move_speed += MOVE_INCREMENT
