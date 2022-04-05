from pickle import TRUE
import pygame
import random
from sys import exit
from boss import Boss
import const
from player import Player
from button import Button
from trigger import Trigger


def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("Graphics/font.ttf", size)


#bruh
class StateManager():

    def __init__(self):
        self.level = 1

    def options(self):
        gameOver = False

        bgSurface = pygame.Surface((800,600))
        bgSurface.fill('Green')

        BACK_BUTTON = Button(280, 500, const.backButtonPath)

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.rect.collidepoint(pygame.mouse.get_pos()):
                        self.level = 1
                        self.stateManager()
                    

            display.blit(bgSurface,(0,0))
            display.blit(BACK_BUTTON.image, (280, 500))
            #display.blit(OPTIONS_BUTTON.image, (125, 150))
            #display.blit(QUIT_BUTTON.image, (230, 250))

            pygame.display.update()
            clock.tick(const.FPS)

    #TODO: main menu
    def mainMenu(self):
        gameOver = False

        bgSurface = pygame.Surface((800,600))
        bgSurface.fill('Blue')

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(69).render("MAIN MENU", True, "#ffb700")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(280, 150, const.playButtonPath)
        OPTIONS_BUTTON = Button(220,280, const.optionsButtonPath)
        QUIT_BUTTON = Button(280, 410, const.quitButtonPath)
        
        buttonGroup = pygame.sprite.Group()

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
                        self.level = 2
                        self.stateManager()
                    if OPTIONS_BUTTON.rect.collidepoint(pos):
                        self.level = 3
                        self.stateManager()
                    if QUIT_BUTTON.rect.collidepoint(pos):
                        pygame.quit()
                        exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()


            display.blit(bgSurface,(0,0))
            display.blit(MENU_TEXT, (85, 33))
            display.blit(PLAY_BUTTON.image, (280, 150))
            display.blit(OPTIONS_BUTTON.image, (220,280))
            display.blit(QUIT_BUTTON.image, (280,410))
            #display.blit(OPTIONS_BUTTON.image, (125, 150))
            #display.blit(QUIT_BUTTON.image, (230, 250))

            pygame.display.update()
            clock.tick(const.FPS)

    #game loop
    def game(self):
        gameOver = False

        jumpingTimer = 120

        #triggers
        testTrigger = Trigger(730, 550, 20, 20)
        triggerGroup = []
        triggerGroup.append(testTrigger)

        background = pygame.image.load(const.gameBackgroundPath)
        bgScaled = pygame.transform.scale(background, (800, 600))
        floor_surface= pygame.image.load(const.floorPath)
        platform_surface=pygame.image.load(const.platformPath)
        platform_surface=pygame.transform.scale(platform_surface, (178, 52))
        platform_list=[]
        platform_height= [200, 300, 400, 500]
        boss = Boss(300, 408, const.bossSpritePath, 100)
        spawn_platform=pygame.USEREVENT
        pygame.time.set_timer(spawn_platform, const.spawn_platform_time)
        #creating the player
        player = Player(300, 408, const.playerSpritePath, 100)
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)
        #score
        score = 0
        score_font = get_font(20)
        blood_font = get_font(20)
        def display_score():
            score_surface=score_font.render(f'Score:{int(score)}', True, const.white)
            score_rect=score_surface.get_rect(center=(700, 80))
            display.blit(score_surface, score_rect)
        def display_blood():
            blood_surface=blood_font.render(f'Health:{int(player.blood)}', True, const.red_blood)
            blood_rect = blood_surface.get_rect(center=(110, 80))
            display.blit(blood_surface, blood_rect)
        def draw_floor():
            display.blit(floor_surface, (const.floor_x_position, 450))
            display.blit(floor_surface, (const.floor_x_position+800, 450)) 
        def create_platform():
            platform_x_position=random.choice(platform_height)
            new_platform=platform_surface.get_rect(midbottom=(900, platform_x_position))
            return new_platform
        def move_platforms(platforms):
            for platform in platforms:
                platform.centerx-=2
            return platforms
        def draw_platforms(platforms):
            for platform in platforms:
                display.blit(platform_surface, platform)



        #sounds 
        bryh_sound=pygame.mixer.Sound(const.bryhsound)

        #TODO: change the background

        while not gameOver:
            player.collisionWIthFloor(floor_surface)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #KEYDOWN EVENTS
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jumpingTimer -= 1
                        const.playerMovement -= 89
                        const.isJumped = True
                    if event.key == pygame.K_a:
                        player.leftPressed = True
                        bryh_sound.play()
                    if event.key == pygame.K_d:
                        player.rightPressed = True
                        bryh_sound.play()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            exit()
                if event.type==spawn_platform:
                    platform_list.append(create_platform())

                #KEYUP EVENTS
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player.leftPressed = False
                    if event.key == pygame.K_d:
                        player.rightPressed = False
                    if event.key == pygame.K_w:
                        player.upPressed = False

                if player.rect.colliderect(testTrigger.rect):
                    testTrigger.action()
                    
            if const.isJumped:
                jumpingTimer -= 1
                if jumpingTimer == 0:
                    const.isJumped = False
                    jumpingTimer = 120

            player.update()
            display.blit(bgScaled, (0, 0))
            #blit triggers
            for trigger in triggerGroup:
                display.blit(trigger.trigger, (trigger.x, trigger.y))
            display.blit(player.image,(player.rect.x, player.rect.y))
            display.blit(boss.image, (boss.rect.x, boss.rect.y))
            display_score()
            score+=0.04
            platform_list=move_platforms(platform_list) 
            draw_platforms(platform_list)
            display_blood()
            const.floor_x_position-=2
            draw_floor()
            if const.floor_x_position<=-800:
                const.floor_x_position=0
            
            pygame.display.update()
            #bruh
            clock.tick(const.FPS)

    def stateManager(self):
        if self.level == 1:
            self.mainMenu()
        if self.level == 2:
            self.game()
        if self.level == 3:
            self.options()

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
