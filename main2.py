# Бросок под углом к горизонту
import math
import turtle

turtle.speed(1)
turtle.penup()
x = 0
y = 0
turtle.pendown()

g = 1 #float(input())
Vx = 8 #float(input())
Vy = 25 #float(input())
t = 0

for i in range(1000):
    t += 1
    x += Vx
    y += Vy - g*t
    if y <= 0:
        Vy = 0.7*math.sqrt((g*t - Vy)**2)
        t = 0
    turtle.goto(x, y)


