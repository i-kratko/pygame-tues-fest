import pygame
from sys import exit
import const
from player import Player


#bruh
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

            display.blit(test_surface,(0,0))

            pygame.display.update()
            clock.tick(const.FPS)

    #game loop
    def game(self):
        gameOver = False

        #creating the player
        player = Player(0, 0, const.playerSpritePath)
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            player.update()

            display.blit(player.image,(player.rect.x, player.rect.y))

            pygame.display.update()
            clock.tick(const.FPS)

    def stateManager(self):
        if self.level == 1:
            #TODO: change strating scene to main menu
            self.game()

#innit
pygame.init()
display = pygame.display.set_mode((const.disW, const.disH))
pygame.display.set_caption(const.gameName)
clock = pygame.time.Clock()
     
stateManager = StateManager()

#gameloop
def gameLoop():
    while True:
        stateManager.stateManager()

gameLoop()
    