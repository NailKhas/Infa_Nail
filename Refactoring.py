import pygame
import numpy as np
from pygame.draw import *
from random import *

pygame.init()

FPS = 30
WHITE = (255, 255, 255)
YELLOW = (255, 255, 51)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (204, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 153, 51)
BROWN = (204, 102, 0)
LIGHT_BROWN = (255, 204, 153)

screen = pygame.display.set_mode((536, 758))
screen.fill(WHITE)


def draw_hedge(surface, x, y, size, body_color=BROWN, spikes_color=BLACK, eyes_color=LIGHT_BLUE):
    '''
    :param surface: поверхность для ежжика
    :param x: центр тела ежжика по х
    :param y: центр тела ежжика по у
    :param size: размера ежжика (1 -- для самого большого (при желании можно и больше) разера ежжика)
    :param body_color: цвет тела ежжика
    :param spikes_color: цвет колючек ежжика
    :param eyes_color: цвет глаз ежжика
    :return: нарисованный ежжик
    '''
    draw_hedge_body(surface, x, y, size, body_color)
    draw_hedge_head(surface, x, y, size, body_color)
    draw_hedge_spikes()


def draw_hedge_body(body_surface, bodyx, bodyy, body_size, body_color):
    '''

    :param body_surface: поверхность для тела ежжика
    :param bodyx: очевидно
    :param bodyy: очевидно
    :param body_size: размер тела ежжика (1 -- для самого большого (при желании можно и больше) разера ежжика)
    :param body_color: цвет тела ежжика
    :return: тело ежжка с ногами в кол-ве 4 шт.
    '''
    ellipse(body_surface, body_color, (bodyx, bodyy, 210 * body_size, 100 * body_size))
    ellipse(body_surface, body_color, (bodyx + 160 * body_size, bodyy + 80 * body_size, 30 * body_size, 20 * body_size))
    ellipse(body_surface, body_color, (bodyx + 180 * body_size, bodyy + 65 * body_size, 30 * body_size, 20 * body_size))
    ellipse(body_surface, body_color, (bodyx - 10 * body_size, bodyy + 65 * body_size, 30 *  body_size, 20 * body_size))
    ellipse(body_surface, body_color, (bodyx + 10 * body_size, bodyy + 80 * body_size, 30 *  body_size, 20 * body_size))


def draw_hedge_head(head_surface, head_x, head_y, head_size, head_color, eyes_color):
    '''
    :param head_surface: поверхность для головы ежжка
    :param head_x: координата х центра тела, к которому крепится голова ежжика
    :param head_y: координата х центра тела, к которому крепится голова ежика
    :param head_size: размер головы ежжика (1 -- для самого большого (при желании можно и больше) разера ежжика)
    :param head_color: цвет головы ежжика
    :param eyes_color: цвет глаз ежжика
    :return:
    '''
    ellipse(screen, head_color, (head_x + 185 * head_size, head_y + 35 * head_size, 80 * head_size, 40 * head_size))
    circle(screen, BLACK, (head_x + 262 * head_size, head_y + 55 * head_size), 5 * head_size)    #nose
    circle(screen, eyes_color, (head_x + 215 * head_size, head_y + 50 * head_size), 8 * head_size)    #eyes
    circle(screen, eyes_color, (head_x + 235 * head_size, head_y + 40 * head_size), 8 * head_size)
    circle(screen, BLACK, (head_x + 215 * head_size, head_y + 50 * head_size), 3 * head_size)
    circle(screen, BLACK, (head_x + 235 * head_size, head_y + 40 * head_size), 3 * head_size)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
