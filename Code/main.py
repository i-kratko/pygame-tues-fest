from pickle import TRUE
import pygame
import random
from sys import exit
from boss import Boss
import const
from weapon import Weapon
from player import Player
from button import Button
from trigger import Trigger
from enemy import Enemy
from random import randint
from platform import Platform

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
        platform_surface=pygame.image.load(const.platformPath)
        platform_surface=pygame.transform.scale(platform_surface, (178, 52))
        platform_list = pygame.sprite.Group()
        platform_height= [175, 275, 375]
        spawn_platform=pygame.USEREVENT 
        pygame.time.set_timer(spawn_platform, const.spawn_platform_time)    
        spawn_enemy=pygame.USEREVENT+1
        ##PLAT COUNTER
        self.platformCounter = 0
        #creating the player
        player = Player(40, 418, const.playerSpritePath, 100)
        enemy = Enemy(500, 392, const.enemySpritePath, 100)
        enemy_list=[]
        boss = Boss(0, 0, const.bossSpritePath, 500)
        dagger = Weapon(350,418, const.daggerSpritePath, 20)
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
        def create_platform():
                platform_y_position=random.choice(platform_height)
                new_platform = Platform(900, platform_y_position, const.platformSpritePath)
                return new_platform
        def move_platforms(platforms):
            for platform in platforms:
                platform.update()
            return platforms
        def draw_platforms(platforms):
            for platform in platforms:
                enemy.drawEnemy(platform.rect.centerx-36, platform.rect.top-42, display)
                dagger.drawWeapon(platform.rect.centerx+30, platform.rect.top-16, display)
                display.blit(platform.image, (platform.x, platform.y))
        def create_enemy(): 
            enemy_x_position=random.choice(platform_height)
            new_enemy = Enemy(500, enemy_x_position+30, const.enemySpritePath, 100)
            new_enemy=new_enemy.rect(midbottom=(300, enemy_x_position+30))
            return new_enemy
        def move_enemy(enemies):
            for enemy in enemies:
                Enemy.centerx-=2
            return enemies
        def draw_enemy(enemies):
            for enemy in enemies:
                display.blit(Enemy.image, enemy)

        def checkPlatformCollisionWithPLayer(platforms):
            for platform in platforms:
                if platform.rect.colliderect(player.rect):
                    player.isStanding = True
                    break
                else:
                    player.isStanding = False
                #TODO
                #if platform.x < -200:
                    

        #sounds 
        bryh_sound=pygame.mixer.Sound(const.bryhsound)

        #TODO: change the background

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player.animateSelf()
                #KEYDOWN EVENTS
                if event.type==spawn_platform:
                    platform_list.add(create_platform())
                    print("BREH")
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and const.isJumped == False:
                        jumpingTimer -= 1
                        const.playerMovement -= 89
                        const.isJumped = True
                    if event.key == pygame.K_a:
                        player.leftPressed = True
                        bryh_sound.play()
                    if event.key == pygame.K_d:
                        player.rightPressed = True
                        bryh_sound.play()
                    if event.key == pygame.K_SPACE:
                        player.jumpPressed = True
                        bryh_sound.play()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.level = 1
                            self.stateManager()
                #KEYUP EVENTS
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player.leftPressed = False
                    if event.key == pygame.K_d:
                        player.rightPressed = False
                    if event.key == pygame.K_SPACE:
                        player.jumpPressed = False
                        bryh_sound.play()

                if player.rect.colliderect(testTrigger.rect):
                    testTrigger.action()

            player.update()
            player.updateSprite()
            dagger.pickUp(player)
            if player.rect.bottom > 450:
                const.playerMovement += const.gravity
            player.rect.centery += const.playerMovement
            display.blit(bgScaled, (0, 0))

            checkPlatformCollisionWithPLayer(platform_list)

            display.blit(player.image,(player.rect.x, player.rect.y))
            #display.blit(boss.image, (boss.rect.x, boss.rect.y))
            display_score()
            score += 0.04
            #platform_list = move_platforms(platform_list) 
            platform_list.update()
            draw_platforms(platform_list)
            enemy_list=move_enemy(enemy_list)
            draw_enemy(enemy_list)
            display_blood()
            
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
