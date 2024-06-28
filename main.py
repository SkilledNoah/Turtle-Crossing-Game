"""
---------------------------------------
    * Course: 100 Days of Code - Dra. Angela Yu
    * Author: Noah Louvet
    * Day: 23 - Turtle crossing game
    * Subject: Tkinter GUI - OOP
---------------------------------------
"""

import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("grey")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

line = Turtle()
line.hideturtle()
line.penup()
line.setheading(180)
y_pos = -250
while y_pos < 240:
    line.color("white")
    line.goto(600, y_pos)
    if y_pos == -10:
        line.color("orange")
    for _ in range(30):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(15)
    y_pos += 80

game_is_on = True
counter = 0

while game_is_on:
    time.sleep(0.05)
    screen.update()

    if counter % 6 == 0:
        car_manager.create_car()
    car_manager.car_move()

    # Detect finish line
    if player.ycor() == 280:
        scoreboard.increase_level()
        car_manager.increase_difficulty()
        player.reset_position()

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    counter += 1

screen.exitonclick()
