import pygame
from pygame import sprite
import const

class Boss(pygame.sprite.Sprite):
    def __init__(self, x, y, spritePath, health):
        super().__init__()
        self.image = pygame.image.load(const.bossSpritePath)
        self.image = pygame.transform.scale(self.image, (38, 40))
        self.rect = self.image.get_rect()
        self.x = int(x)
        self.y = int(y)
        self.velX = 0
        self.velY = 0
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
        self.health = 500
