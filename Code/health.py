import pygame
from pygame import sprite
from player import Player
from enemy import Enemy
import const
import random

class Health(pygame.sprite.Sprite):
    def __init__(self, x, y, spritePath, healthRestore, heartPicked):
        super().__init__()
        self.heartPicked = heartPicked
        self.image = pygame.image.load(spritePath)
        self.image = pygame.transform.scale(self.image, (28, 30))
        self.rect = self.image.get_rect()
        self.x = int(x)
        self.y = int(y)
        self.rect.x = self.x
        self.rect.y = self.y
        self.healthRestore = healthRestore

    def restoreHealth(self, player):
        player.health += self.healthRestore