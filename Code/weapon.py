import pygame
from pygame import sprite
from player import Player
import const

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, spritePath, damage):
        super().__init__()
        self.image = pygame.image.load(spritePath)
        self.image = pygame.transform.scale(self.image, (28, 30))
        self.rect = self.image.get_rect()
        self.x = int(x)
        self.y = int(y)
        self.damage = int(damage)

    def pickUp(self, player):
        if self.rect.colliderect(player):
            print("bruH")