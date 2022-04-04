from pickle import TRUE
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

    def play(self):
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            display.fill("black")

            PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            display.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.mainMenu()


            pygame.display.update()
    
    def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            display.fill("white")

            OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            display.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.mainMenu()

            pygame.display.update()


    #TODO: main menu
    def mainMenu(self):
        gameOver = False

        bgSurface = pygame.Surface((800,600))
        bgSurface.fill('Blue')

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(None, pos=(640, 250), text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        OPTIONS_BUTTON = Button(None, pos=(640, 400), text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")
        QUIT_BUTTON = Button(None, pos=(640, 550), text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="Green")

        display.blit(MENU_TEXT, (0, 0))

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(display)

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    #if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                            #print("BRUH")
                            #self.level = 2
                            #self.stateManager()
                    if PLAY_BUTTON.rect.collidepoint(pos):
                        print("BRUH")
                        self.level = 2
                        self.stateManager()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()


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
        player = Player(10, 10, const.playerSpritePath)
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)
        #score
        score = 0
        score_font = get_font(20)
        def display_score():
            score_surface=score_font.render(f'Score:{int(score)}', True, const.white)
            score_rect=score_surface.get_rect(center=(700, 100))
            display.blit(score_surface, score_rect)
        #sounds 
        bryh_sound=pygame.mixer.Sound(const.bryhsound)

        #TODO: change the background

        bg = pygame.Surface((800,600))
        bg = pygame.image.load(const.backgroundPath)

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #KEYDOWN EVENTS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        player.leftPressed = True
                        bryh_sound.play()
                    if event.key == pygame.K_d:
                        player.rightPressed = True
                        bryh_sound.play()
                    if event.key == pygame.K_w:
                        player.upPressed = True
                        bryh_sound.play()
                    if event.key == pygame.K_s:
                        player.downPressed = True
                        bryh_sound.play()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            exit()
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
            display_score()
            score+=0.04

            pygame.display.update()
            clock.tick(const.FPS)

    def stateManager(self):
        if self.level == 1:
            self.mainMenu()
        if self.level == 2:
            self.game()

#innit
pygame.mixer.pre_init(frequency=44100, size=16, channels=1, buffer=256)
pygame.init()
display = pygame.display.set_mode((const.disW, const.disH), pygame.FULLSCREEN)
pygame.display.set_caption(const.gameName)
clock = pygame.time.Clock()
     
stateManager = StateManager()
    
#gameloop
def gameLoop():
    while True:
        stateManager.stateManager()

gameLoop()
