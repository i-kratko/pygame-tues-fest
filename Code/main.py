from turtle import width
import pygame
from sys import exit




class StateManager():
    def __init__(self):
        self.level = 1

    #TODO: adekvatno ime
    def start(self):
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
            clock.tick(60)

    def stateManager(self):
        if self.level == 1:
            self.start()

#innit
pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Test')
clock = pygame.time.Clock()
     
stateManager = StateManager()

#gameloop
def gameLoop():
    while True:
        stateManager.stateManager()

gameLoop()
    