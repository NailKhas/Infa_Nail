import pygame
from pygame.draw import *
from random import randint
pygame.font.init()

pygame.init()

FPS = 1
screen = pygame.display.set_mode((500, 500))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    """рисует новый шарик """
    global x, y, r
    x = randint(50, 450)
    y = randint(50, 450)
    r = randint(10, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

new_ball()
score = 0

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            global x, y, r
            if (pygame.mouse.get_pos()[0] - x) ** 2 + (pygame.mouse.get_pos()[1] - y) ** 2 < r ** 2:
                score += 51 - r
                new_ball()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()
