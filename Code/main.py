from turtle import width
import pygame
from sys import exit
import const

class StateManager():
    def __init__(self):
        self.level = 1

    #main menu
    def mainMenu(self):
        gameOver = False

        test_surface = pygame.Surface((200,300))
        test_surface.fill('Blue')

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            screen.blit(test_surface,(0,0))

            pygame.display.update()
            clock.tick(const.FPS)

    #game loop
    def game():
        gameOver = False

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

        pygame.display.update()
        clock.tick(const.FPS)

    def stateManager(self):
        if self.level == 1:
            self.mainMenu()

#innit
pygame.init()
screen = pygame.display.set_mode((const.disW, const.disH))
pygame.display.set_caption(const.gameName)
clock = pygame.time.Clock()
     
stateManager = StateManager()

#gameloop
def gameLoop():
    while True:
        stateManager.stateManager()

gameLoop()
    