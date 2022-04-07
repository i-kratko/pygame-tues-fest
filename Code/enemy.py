import pygame
from pygame import sprite
import const
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, spritePath, health):
        super().__init__()
        self.sprites = []
        self.isAnimating = False
        self.sprite1 = pygame.image.load("Graphics/Enemies/Enemy Animations/enemy2_1.png.png")
        self.sprite1 = pygame.transform.scale(self.sprite1, (72, 72))
        self.sprite2 = pygame.image.load("Graphics/Enemies/Enemy Animations/enemy2_2.png.png")
        self.sprite2 = pygame.transform.scale(self.sprite2, (72, 72))
        self.sprites.append(pygame.image.load("Graphics/Enemies/Enemy Animations/enemyIdle.png"))
        self.sprites.append(self.sprite1)
        self.sprites.append(self.sprite2)
        self.currentSprite = 0
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

    def stopAnimation(self):
        self.isAnimating = False

    def updateSprite(self):
        if self.isAnimating == True:
            self.currentSprite += 0.25
            if self.currentSprite >= len(self.sprites):
                self.currentSprite = 0
            
            self.image = pygame.transform.scale(self.sprites[int(self.currentSprite)], (72, 72))

    def drawEnemy(self, x, y, display):
        display.blit(self.image, (x,y))

    def takeDamage(self, player):
        self.health -= player.damage
        if player.blood < 100:
            player.blood += 3
        if self.health <= 0:
            self.stun()
    
    def stun(self):
        self.isAnimating = True