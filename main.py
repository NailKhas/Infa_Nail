# Броуновское движение
import turtle
from random import *

turtle.shape('turtle')
turtle.speed(0)

for i in range(0, 1000, 1):
    turtle.forward(randint(0, 50))
    turtle.left(randint(-180, 180))


