import pygame
from pygame import sprite
import const

#rework class to remove vertical movement

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, spritePath, blood, damage):
        super().__init__()
        self.attackSprites = []
        self.isAnimating = False
        self.attackSprites.append(pygame.image.load("Graphics/Player/idle.png"))
        self.attackSprites.append(pygame.image.load("Graphics/Player/swing1.png"))
        self.attackSprites.append(pygame.image.load("Graphics/Player/swing2.png"))
        self.currentSprite = 0
        self.image = self.attackSprites[self.currentSprite]
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
        self.blood = blood
        self.damage = damage
    
    def animateSelf(self):
        self.isAnimating = True

    def updateSprite(self):
        if self.isAnimating == True:
            self.currentSprite += 0.16
            if self.currentSprite >= len(self.attackSprites):
                self.currentSprite = 0
                self.isAnimating = False
            
            self.image = self.attackSprites[int(self.currentSprite)]

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

        self.isStandingOnPlatform()

        if self.jumpPressed is True:
            self.velY -= 100

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(int(self.x), int(self.y), 32, 58)        

        