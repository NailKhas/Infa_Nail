import random
import pygame
from pygame.draw import *

FPS = 30
pygame.init()
screen = pygame.display.set_mode((400, 400))
number_of_balls = 1


def handle_events(x, y, finished):
    """
    Функция обрабатывает нажатия мышки
    :param x: абцисса нажатия
    :param y: ордината нажатия
    :param finished: существование нажатия
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
    return finished, x, y


def game_process(xcirc, ycirc, x, y, rad, score, ball_speed):
    """
    Функция проверяет попадание по шарику и начисляет очки
    :param xcirc: абцисса центра шарика
    :param ycirc: ордината центра шарика
    :param x: абцисса нажатия
    :param y: ордината нажатия
    :param rad: радиус шарика
    :param score: счет
    :param ball_speed: скорость шарика по соответствующей оси
    """
    for i in range(number_of_balls):
        if (x - xcirc[i]) ** 2 + (y - ycirc[i]) ** 2 < rad[i] ** 2:
            f = pygame.font.Font(None, 36)
            rect(screen, (0, 0, 0), (10, 10, 130, 40))
            score += 50 - rad[i]
            text = f.render('Score:' + str(score), True, (180, 0, 0))
            screen.blit(text, (10, 10))
            xcirc[i], ycirc[i], rad[i], ball_speed[i] = new_ball(xcirc[i], ycirc[i], rad[i], ball_speed[i])
    for i in range(len(xcirc)):
        xcirc[i], ycirc[i], rad[i], ball_speed[i] = move_ball(xcirc[i], ycirc[i], rad[i], ball_speed[i])
    return xcirc, ycirc, rad, score, ball_speed


def move_ball(xcirc, ycirc, rad, ball_speed):
    """
    Функци двигает шарики
    :param xcirc: абцисса шарика
    :param ycirc: ордината шарика
    :param rad: радиус шарика
    :param ball_speed: скорость шарика по соответствующей оси
    """
    circle(screen, (0, 0, 0), (xcirc, ycirc), rad)
    if xcirc + ball_speed[0] > 400 - rad and xcirc > rad:
        ball_speed[0] = -ball_speed[0]
    elif xcirc + ball_speed[0] < rad and xcirc < rad:
        ball_speed[0] = -ball_speed[0]
    if ycirc + ball_speed[1] > 400 - rad and ycirc > rad:
        ball_speed[1] = -ball_speed[1]
    elif ycirc + ball_speed[1] < 40 + rad and ycirc < 40 + rad:
        ball_speed[1] = -ball_speed[1]
    ycirc += ball_speed[1]
    xcirc += ball_speed[0]
    circle(screen, (random.randint(0, 250), random.randint(0, 250), random.randint(0, 250)), (xcirc, ycirc), rad)
    return xcirc, ycirc, rad, ball_speed


def new_ball(xcirc, ycirc, rad, ball_speed):
    """
    Функция рисует новые шарики
    :param xcirc: абцисса центра шарика
    :param ycirc: ордината центра шарика
    :param rad: радиус шарика
    :param ball_speed: скорость шарика по соответствующей оси
    """
    circle(screen, (0, 0, 0), (xcirc, ycirc), rad)
    ycirc = random.randint(90, 350)
    xcirc = random.randint(50, 350)
    rad = random.randint(12, 50)
    ball_speed[0] = random.randint(-8, 8)
    ball_speed[1] = random.randint(-8, 8)
    circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (xcirc, ycirc), rad)
    return xcirc, ycirc, rad, ball_speed


ycirc = [None] * number_of_balls
xcirc = [None] * number_of_balls
rad = [None] * number_of_balls
color = [None] * number_of_balls
ball_speed = []
for i in range(number_of_balls):
    ycirc[i] = random.randint(20, 380)
    xcirc[i] = random.randint(20, 380)
    rad[i] = random.randint(20, 50)
    color[i] = (random.randint(0, 250), random.randint(0, 250), random.randint(0, 250))
    ball_speed.append([random.randint(10, 50), random.randint(10, 50)])

for i in range(number_of_balls):
    xcirc[i], ycirc[i], rad[i], ball_speed[i] = new_ball(ycirc[i], xcirc[i], rad[i], ball_speed[i])

pygame.display.update()
clock = pygame.time.Clock()
finished = False
x = 0
y = 0
score = 0

while not finished:
    clock.tick(FPS)
    finished, x, y = handle_events(x, y, finished)
    xcirc, ycirc, rad, score, ball_speed = game_process(xcirc, ycirc, x, y, rad, score, ball_speed)
    x = 800
    y = 800
    pygame.display.update()

pygame.quit()
