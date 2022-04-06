import pygame
from pygame import sprite
import const
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, spritePath, health):
        super().__init__()
        self.image = pygame.image.load(const.enemySpritePath)
        self.image = pygame.transform.scale(self.image, (72, 72))
        self.rect = self.image.get_rect()
        self.x = int(x)
        self.y = int(y)
        self.rect.x = self.x
        self.rect.y = self.y
        self.rightPressed = False
        self.leftPressed = False
        self.upPressed = False
        self.downPressed = False
        self.facingRight = True
        self.facingLeft = False
        self.facingUp = False
        self.facingDown = False
        self.speed = 10
        self.health = health

    def drawEnemy(self, x, y, display):
        if random.randint(0,100) < 33:
            display.blit(self.image, (x,y))