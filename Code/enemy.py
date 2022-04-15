import pygame
from pygame import sprite
import const
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, spritePath, health):
        super().__init__()
        self.sprites = []
        self.currentSprite = 0
        self.sprite1 = pygame.image.load("Graphics/Enemies/Enemy Animations/dragon-1.png.png")
        self.sprite2 = pygame.image.load("Graphics/Enemies/Enemy Animations/dragon-2.png.png")
        self.sprite3 = pygame.image.load("Graphics/Enemies/Enemy Animations/dragon-3.png.png")
        self.sprite4 = pygame.image.load("Graphics/Enemies/Enemy Animations/dragon-4.png.png")
        self.sprites.append(self.sprite1)
        self.sprites.append(self.sprite2)
        self.sprites.append(self.sprite3)
        self.sprites.append(self.sprite4)
        self.image = pygame.transform.scale(self.sprites[self.currentSprite], (72, 72))
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

    def update(self):
            self.currentSprite += 0.16
            if self.currentSprite >= len(self.sprites):
                self.currentSprite = 0
            
            self.image = pygame.transform.scale(self.sprites[int(self.currentSprite)], (72, 72))

    def drawEnemy(self, x, y, display):
        display.blit(self.image, (x,y))

    def takeDamage(self, player):
        self.health -= player.weapon.damage
        print(self.health)
        if self.health <= 0:
            self.rect.y = -420.69