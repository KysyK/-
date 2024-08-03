import pygame
from pygame.examples.moveit import WIDTH, HEIGHT
from settings import *

from settings import FPS

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    if game:
        ...

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()

