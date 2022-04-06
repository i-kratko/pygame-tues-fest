import pygame
from pygame import sprite
from player import Player
from enemy import Enemy
import const
import random

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, spritePath, damage):
        super().__init__()
        self.image = pygame.image.load(spritePath)
        self.image = pygame.transform.scale(self.image, (28, 30))
        self.rect = self.image.get_rect()
        self.x = int(x)
        self.y = int(y)
        self.rect.x = self.x
        self.rect.y = self.y
        self.damage = int(damage)

    def pickUp(self, player):
        if self.rect.colliderect(player.rect):
            print("leko mi e bruh.")
    
    def dealDamage(self, enemy):
        enemy.hitpoints -= self.damage
        print(enemy.hitpoints)
    
    def drawWeapon(self, x, y, display):
        if random.randint(0,100) < 33:
            display.blit(self.image, (x,y))