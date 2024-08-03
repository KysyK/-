import pygame
from settings import *

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, w, h, speed):
        super().__init__()
        self.w = w
        self.h = h
        self.speed = speed
        self.image = pygame.transform.scale(image, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

