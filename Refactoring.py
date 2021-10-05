import pygame
import numpy as np
from pygame.draw import *
from random import *

pygame.init()

FPS = 30
SCREEN_WIDTH = 536
SCREEN_HEIGHT = 758
WHITE = (255, 255, 255)
YELLOW = (255, 255, 51)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_BLUE = (204, 255, 255)
BLUE = (0, 0, 255)
ORANGE = (255, 153, 51)
BROWN = (204, 102, 0)
LIGHT_BROWN = (255, 204, 153)
GROUND_BROWN = (105, 85, 55)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(LIGHT_BLUE)


def draw_hedge(surface, x, y, spikes_number, size=1, body_color=BROWN, spikes_color=BLACK, eyes_color=LIGHT_BLUE):
    '''
    :param surface: поверхность для ежжика
    :param x: координата х тела ежжика
    :param y: координата у тела ежжика
    :param spikes_number: кол-во колючек ежжика
    :param size: размера ежжика (1 -- для самого большого (при желании можно и больше) разера ежжика)
    :param body_color: цвет тела ежжика
    :param spikes_color: цвет колючек ежжика
    :param eyes_color: цвет глаз ежжика
    :return: нарисованный ежжик
    '''
    draw_hedge_body(surface, x, y, size, body_color)
    draw_hedge_head(surface, x, y, size, body_color, eyes_color)
    draw_hedge_spikes(surface, x, y, size, spikes_color, spikes_number)


def draw_hedge_body(body_surface, bodyx, bodyy, body_size, body_color):
    '''

    :param body_surface: поверхность для тела ежжика
    :param bodyx: координата х тела ежжика
    :param bodyy: координата у тела ежжика
    :param body_size: размер тела ежжика (1 -- для самого большого (при желании можно и больше) разера ежжика)
    :param body_color: цвет тела ежжика
    :return: тело ежжка с ногами в кол-ве 4 шт.
    '''
    ellipse(body_surface, body_color, (bodyx, bodyy, 210 * body_size, 100 * body_size))
    ellipse(body_surface, body_color, (bodyx + 160 * body_size, bodyy + 80 * body_size, 30 * body_size, 20 * body_size))
    ellipse(body_surface, body_color, (bodyx + 180 * body_size, bodyy + 65 * body_size, 30 * body_size, 20 * body_size))
    ellipse(body_surface, body_color, (bodyx - 10 * body_size, bodyy + 65 * body_size, 30 *  body_size, 20 * body_size))
    ellipse(body_surface, body_color, (bodyx + 10 * body_size, bodyy + 80 * body_size, 30 *  body_size, 20 * body_size))


def draw_hedge_head(head_surface, body_x, body_y, head_size, head_color, eyes_color):
    '''
    :param head_surface: поверхность для головы ежжка
    :param body_x: координата х тела ежжика
    :param body_y: координата у тела ежжика
    :param head_size: размер головы ежжика (1 -- для самого большого (при желании можно и больше) разера ежжика)
    :param head_color: цвет головы ежжика
    :param eyes_color: цвет глаз ежжика
    :return:
    '''
    ellipse(head_surface, head_color, (body_x + 185 * head_size, body_y + 35 * head_size, 80 * head_size, 40 * head_size))
    circle(head_surface, BLACK, (body_x + 262 * head_size, body_y + 55 * head_size), 5 * head_size)    #nose
    circle(head_surface, eyes_color, (body_x + 215 * head_size, body_y + 50 * head_size), 8 * head_size)    #eyes
    circle(head_surface, eyes_color, (body_x + 235 * head_size, body_y + 40 * head_size), 8 * head_size)
    circle(head_surface, BLACK, (body_x + 215 * head_size, body_y + 50 * head_size), 3 * head_size)
    circle(head_surface, BLACK, (body_x + 235 * head_size, body_y + 40 * head_size), 3 * head_size)


def draw_hedge_spikes(spikes_surface, body_x, body_y, spikes_size, spikes_color, spikes_number):
    '''
    :param spikes_surface: поверхность для колючек ежжика
    :param body_x: координата х тела ежжика
    :param body_y: координата у тела ежжика
    :param spikes_size: размер колючек ежжика  (1 -- для самого большого (при желании можно и больше) разера ежжика) 
    :param spikes_color: цвет колючек ежжика
    :param spikes_number: количесвто колючек ежжика
    :return: Рисует колючки ежжика
    '''
    for count_spikes in range(spikes_number):
        spike_x = randint((body_x + 20 * spikes_size) // 1, (body_x + 180 * spikes_size) // 1)
        spike_y = randint(body_y, (body_y + 70 * spikes_size) // 1)
        spike_rotation_degree = randint(-45, 46) / 180 * np.pi
        spike_end = (spike_x + np.sin(spike_rotation_degree) * 80 * spikes_size, spike_y - np.cos(spike_rotation_degree) * 60 * spikes_size)
        spike_right = (spike_x + np.sin(spike_rotation_degree + 5 / 9 * np.pi) * 20 * spikes_size,
                       spike_y - np.cos(spike_rotation_degree + 5 / 9 * np.pi) * 20 * spikes_size)
        spike_left = (spike_x + np.sin(spike_rotation_degree - 5 / 9 * np.pi) * 20 * spikes_size,
                      spike_y - np.cos(spike_rotation_degree - 5 / 9 * np.pi) * 20 * spikes_size)
        polygon(spikes_surface, spikes_color, (spike_end, spike_right, spike_left))


def draw_ground(ground_surface, height, ground_color=GROUND_BROWN):
    '''

    :param ground_surface: поверхность для земли
    :param height: высота земли в процентах
    :param ground_color: цвет земли
    :return: закрашивает часть экрана, создавая таким образом землю
    '''
    rect(ground_surface, ground_color,
         (0, SCREEN_HEIGHT / 100 * (100 - height), SCREEN_WIDTH, SCREEN_HEIGHT / 100 * height + 1))


def draw_tree(tree_surface, tree_x, tree_y, tree_width, tree_color=YELLOW):
    '''

    :param tree_surface:поверхность для отрисовки дерева
    :param tree_x: координата х левого края дерева
    :param tree_y: координата начала дерева
    :param tree_width: ширина ствола дерева
    :param tree_color: цвет дерева
    :return: рисует дерево
    '''
    rect(tree_surface, tree_color, (tree_x, 0, tree_width, tree_y))


draw_ground(screen, 35)
draw_tree(screen, 400, 658, 100)
draw_hedge(screen, 200, 500, 60, size=0.75)
draw_tree(screen, 200, 590, 110)
draw_tree(screen, 0, 650, 50)
draw_hedge(screen, 400, 670, 60, size=0.5)
draw_hedge(screen, 50, 620, 60)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
