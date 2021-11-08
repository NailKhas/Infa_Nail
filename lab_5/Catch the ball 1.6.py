import random

import pygame
from pygame.draw import *


FPS = 30
pygame.init()
screen = pygame.display.set_mode((1000, 800))
Amount_of_balls = 10


def handle_events():
    """
    Обрабатывает нажатие мышки
    """
    finish_clicked = False
    x = screen.get_width() + 1
    y = screen.get_height() + 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish_clicked = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
    return(finish_clicked, x, y)


def game_process(xcirc, ycirc, xclick, yclick, rad, score, ball_speed, colour):
    """
    Проверяет нажатие по шарику
    :param xcirc: абцисса центра шарика
    :param ycirc: ордината центра шарика
    :param xclick: абцисса клика
    :param yclick: ордината клика
    :param rad: массив радиусов шаров
    :param score: счет
    :param ball_speed: массив, проекции скорости на оси OX и OY
    :param colour: массив цетов шаров
    :return:
    """
    for i in range(len(xcirc)):
        if (xclick - xcirc[i])**2 + (yclick - ycirc[i])**2 < rad[i]**2:
            score += 70 - rad[i]
            xcirc[i], ycirc[i], rad[i], ball_speed[i], colour[i] = new_ball(xcirc[i], ycirc[i], rad[i], ball_speed[i])
    for i in range(len(xcirc)):
        xcirc[i], ycirc[i], rad[i], ball_speed[i], colour[i] = move_ball(xcirc[i], ycirc[i], rad[i], ball_speed[i], colour[i])
    return (xcirc, ycirc, rad, score, ball_speed, colour)


def move_ball(xcirc, ycirc, rad, ball_speed, colour):
    """
    Перемещает шары
    :param xcirc: абцисса передвинутого шара
    :param ycirc: ордината передвинутого шара
    :param rad: радиус шара
    :param ball_speed: скорость шара
    :param colour: цвет шара
    """
    circle(screen, (0, 0, 0), (xcirc, ycirc), rad)
    if xcirc + ball_speed[0] > 1000 - rad and xcirc > rad:
        ball_speed[0] = -ball_speed[0]
    elif xcirc + ball_speed[0] < rad and xcirc < rad:
        ball_speed[0] = -ball_speed[0]
    if ycirc + ball_speed[1] > 800 - rad and ycirc > rad:
        ball_speed[1] = -ball_speed[1]
    elif ycirc + ball_speed[1] < rad and ycirc < rad:
        ball_speed[1] = -ball_speed[1]
    ycirc += ball_speed[1]
    xcirc += ball_speed[0]
    circle(screen, colour, (xcirc, ycirc), rad)
    return (xcirc, ycirc, rad, ball_speed, colour)


def new_ball(xcirc, ycirc, rad, ball_speed):
    """
    Создает шары
    :param xcirc: абцисса нового шара
    :param ycirc: ордината нового шара
    :param rad: радису шара
    :param ball_speed: проекции скоростей на оси
    :return:
    """
    circle(screen, (0, 0, 0), (xcirc, ycirc), rad)
    ycirc = random.randint(70, 730)
    xcirc = random.randint(70, 930)
    rad = random.randint(12, 70)
    ball_speed[0] = random.randint(-10, 15)
    ball_speed[1] = random.randint(-10, 10)
    colour = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    circle(screen, colour, (xcirc, ycirc), rad)
    return xcirc, ycirc, rad, ball_speed, colour


def score_to_screen(score):
    """
    Выводит счет на экран
    :param score: счет
    """
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(score), False, (0, 180, 0))
    rect(screen, (0, 0, 0), (0, 0, 200, 200))
    screen.blit(textsurface, (10, 10))
    print(str(score))


ycirc = [None] * Amount_of_balls
xcirc = [None] * Amount_of_balls
rad = [None] * Amount_of_balls
ball_speed = []
colour = []
for i in range(Amount_of_balls):
    ycirc[i] = random.randint(20, 730)
    xcirc[i] = random.randint(20, 930)
    rad[i] = random.randint(12, 70)
    ball_speed.append([random.randint(10,50), random.randint(10, 50)])
    colour.append([0, 0, 0])

for i in range(len(xcirc)):
    xcirc[i], ycirc[i], rad[i], ball_speed[i], colour[i] = new_ball(ycirc[i], xcirc[i], rad[i], ball_speed[i])

pygame.display.update()
clock = pygame.time.Clock()
finished = False
pygame.font.init()
xclick = 0
yclick = 0
score = 0
while not finished:
    clock.tick(FPS)
    score_to_screen(score)
    finished, xclick, yclick = handle_events()
    xcirc, ycirc, rad, score, ball_speed, colour = game_process(xcirc, ycirc, xclick, yclick, rad, score, ball_speed, colour)
    xclick = screen.get_width() + 1
    yclick = screen.get_height() + 1
    pygame.display.update()
pygame.quit()
