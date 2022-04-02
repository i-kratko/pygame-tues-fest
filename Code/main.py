import pygame
from sys import exit
import const
from player import Player
from button import Button


def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("Graphics/font.ttf", size)


#bruh
class StateManager():

    def __init__(self):
        self.level = 1

    #TODO: main menu
    def mainMenu(self):
        gameOver = False

        bgSurface = pygame.Surface((800,600))
        bgSurface.fill('Blue')

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(None, pos=(640, 250), text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(None, pos=(640, 400), text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(None, pos=(640, 550), text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        display.blit(MENU_TEXT, (0, 0))

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(display)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

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
            display.blit(PLAY_BUTTON.image, (230, 50))
            display.blit(OPTIONS_BUTTON.image, (125, 150))
            display.blit(QUIT_BUTTON.image, (230, 250))

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
