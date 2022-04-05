import pygame
from pygame import sprite
import const

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
        self.upPressed = False
        self.downPressed = False
        self.facingRight = True
        self.facingLeft = False
        self.facingUp = False
        self.facingDown = False
        self.speed = 10
        self.blood = 100


        
    def collisionWIthFloor(self, floor):
        if self.rect.colliderect(floor.get_rect()):
            print("bruh")
            const.gravity = 0
        else:
            const.gravity = 0.5


    #function to handle player movement
    def update(self):
        self.velX = 0
        self.velY = 0
        #checking for horizontal input
        if self.leftPressed and not self.rightPressed:
            self.velX -= self.speed
            self.faciingRight = False
            self.facingLeft = True
        if self.rightPressed and not self.leftPressed:
            self.velX += self.speed
            self.facingRight = True
            self.faciingLeft = False

        #checking for vertical input
        if self.upPressed and not self.downPressed:
            self.velY -= self.speed
        if self.downPressed and not self.upPressed:
            self.velY += self.speed

        #dont allow player to go out of the screen
        if self.rect.x + 32 > 799:
            self.x -= 10
            self.velX = 0
        if  self.rect.x  < 1:
            self.x += 10
            self.velX = 0

        if self.rect.y + 32 > 599:
            self.y -= 10
            self.velY = 0
        if  self.rect.y  < 1:
            self.y += 10
            self.velY = 0

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)        