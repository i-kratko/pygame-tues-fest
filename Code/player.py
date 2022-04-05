import pygame
from pygame import sprite
import const

#rework class to remove vertical movement

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, spritePath, blood):
        super().__init__()
        self.image = pygame.image.load(spritePath)
        self.rect = self.image.get_rect()
        self.x = int(x)
        self.y = int(y)
        self.velX = 0
        self.velY = 0
        self.rightPressed = False
        self.leftPressed = False
        self.jumpPressed = False

        self.facingRight = True
        self.facingLeft = False

        self.isStanding = False

        self.speed = 10
        self.blood = 100

    def isStandingOnPlatform(self):
            if self.isStanding:
                self.velY = 0

    #function to handle player movement
    def update(self):
        self.velX = 0
        #always 2 because of gravity
        self.velY = 5

        #checking for horizontal input
        if self.leftPressed and not self.rightPressed:
            self.velX -= self.speed
            self.faciingRight = False
            self.facingLeft = True
        if self.rightPressed and not self.leftPressed:
            self.velX += self.speed
            self.facingRight = True
            self.faciingLeft = False

        #dont allow player to go out of the screen
        if self.rect.x + 32 > 799:
            self.x -= 10
            self.velX = 0
        if  self.rect.x  < 1:
            self.x += 10
            self.velX = 0


        #jumping
        if self.jumpPressed is True:
            self.velY -= 30

        self.isStandingOnPlatform()

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)        

        