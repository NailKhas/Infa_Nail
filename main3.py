# Идеальный газ
from random import randint
import math
import turtle


number_of_turtles = 10
steps_of_time_number = 10000


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.shapesize(0.7)
    unit.penup()
    unit.speed(0)
    unit.goto(randint(-100, 100), randint(-100, 100))
    unit.left(randint(-180, 180))


for i in range(steps_of_time_number):
    for unit in pool:
        x0 = unit.xcor()
        y0 = unit.ycor()
        unit.forward(5)
        a = math.atan((unit.ycor() - y0) / (unit.xcor() - x0)) / math.pi * 180
        if (math.sqrt(unit.xcor() ** 2)) > 100:
            unit.left(180-2*a)
            x0: float = unit.xcor()
            y0: float = unit.ycor()
        if (math.sqrt(unit.ycor() ** 2)) > 100:
            unit.right(2*a)
            x0: float = unit.xcor()
            y0: float = unit.ycor()
