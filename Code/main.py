import pygame
from sys import exit
import const
from player import Player


#bruh
class StateManager():
    def __init__(self):
        self.level = 1


    #TODO: main menu
    def mainMenu(self):
        gameOver = False

        bgSurface = pygame.Surface((800,600))
        bgSurface.fill('Blue')

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.level = 2
                        self.stateManager()

            display.blit(bgSurface,(0,0))

            pygame.display.update()
            clock.tick(const.FPS)

    #game loop
    def game(self):
        gameOver = False

        #creating the player
        player = Player(0, 0, const.playerSpritePath)
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)

        #TODO: change the background

        bg = pygame.Surface((800,600))
        bg.fill(const.black)

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #KEYDOWN EVENTS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player.leftPressed = True
                    if event.key == pygame.K_d:
                        player.rightPressed = True
                    if event.key == pygame.K_w:
                        player.upPressed = True
                    if event.key == pygame.K_s:
                        player.downPressed = True
                #KEYUP EVENTS
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player.leftPressed = False
                    if event.key == pygame.K_d:
                        player.rightPressed = False
                    if event.key == pygame.K_w:
                        player.upPressed = False
                    if event.key == pygame.K_s:
                        player.downPressed = False

            player.update()

            display.blit(bg, (0, 0))
            display.blit(player.image,(player.rect.x, player.rect.y))

            pygame.display.update()
            clock.tick(const.FPS)

    def stateManager(self):
        if self.level == 1:
            self.mainMenu()
        if self.level == 2:
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
    