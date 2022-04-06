import pygame
import const

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, spritePath):
        super().__init__()
        self.image = pygame.image.load(spritePath)
        self.image = pygame.transform.scale(self.image, (178, 52))
        self.rect = self.image.get_rect()
        self.x = int(x)
        self.y = int(y)
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.x -= 2
        self.rect.x = self.x