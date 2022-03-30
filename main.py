from turtle import width
import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))

pygame.display.set_caption('Test')

clock = pygame.time.Clock()

test_surface = pygame.Surface((200,300))
test_surface.fill('Blue')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface,(0,0))

    pygame.display.update()
    clock.tick(60)