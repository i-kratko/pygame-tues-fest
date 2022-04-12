from pickle import TRUE
from shutil import move
import pygame
import random
from sys import exit
from boss import Boss
import const
import saveData
from weapon import Weapon
from player import Player
from button import Button
from trigger import Trigger
from enemy import Enemy
from random import randint
from platform import Platform

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Graphics/font.ttf", size)

score = 0

leaderboard = {
    'firstPlaceName' : "SUS",
    'firstPlaceScore' : 30,
    'secondPlaceName' : "SUSSIA",
    'secondPlaceScore' : 21,
    'thirdPlaceName' : "KLENDI",
    'thirdPlaceScore' : 1
}

leaderboard = saveData.loadData("Code\save.txt")

#bruh
class StateManager():

    def __init__(self):
        self.level = 1
        self.finalScore = 1

    def options(self):
        gameOver = False

        bgSurface = pygame.Surface((800,600))
        bgSurface.fill('Blue')

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
                        mainMenuSound.stop()
                        self.stateManager()

            display.blit(bgSurface,(0,0))
            display.blit(BACK_BUTTON.image, (280, 500))
            pygame.display.update()
            clock.tick(const.FPS)

    #TODO: main menu
    def mainMenu(self):
        print(leaderboard["firstPlaceName"])
        gameOver = False
        mainMenuSound.play()
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
                    mainMenuSound.stop()
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if PLAY_BUTTON.rect.collidepoint(pos):
                        self.level = 2
                        mainMenuSound.stop()
                        ingameSound.play()
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


    def game_Over(self):
        gameOver = False
        bgSurface = pygame.Surface((800,600))
        bgSurface.fill('Black')
        scoreText = get_font(45).render(f'SCORE: {int(self.finalScore)}', True, "#ffffff")
        gameOver_TEXT = get_font(72).render("GAME OVER", True, "#ffffff")  
        QUIT_BUTTON = Button(280, 410, const.quitGameOverButtonPath)
        pressButton1 = get_font(20).render("press any key to", True, "#ffffff")  
        pressButton2 = get_font(20).render("return to the Main Menu", True, "#ffffff")  

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ingameSound.stop()
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if QUIT_BUTTON.rect.collidepoint(pos):
                        pygame.quit()
                        exit()
                if event.type == pygame.KEYDOWN:
                    self.level = 1
                    self.stateManager()


            display.blit(bgSurface,(0,0))
            display.blit(scoreText, (170,110))
            display.blit(gameOver_TEXT, (75,220))
            display.blit(pressButton1, (215,335))
            display.blit(pressButton2, (155,370))
            display.blit(QUIT_BUTTON.image, (280,450))

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
        spawn_enemy=pygame.USEREVENT
        pygame.time.set_timer(spawn_platform, const.spawn_platform_time)    
        ##PLAT COUNTER
        self.platformCounter = 0
        #first platfrom
        firstPlatform = Platform(20, 200, const.platformPath, True, False, False)
        platform_list.add(firstPlatform)
        #creating the player
        dagger = Weapon(350,418, const.daggerSpritePath, 30)
        sword = Weapon(350,418, const.swordSpritePath, 20)
        player = Player(40, 100, const.playerSpritePath, 100, dagger)
        enemy = Enemy(500, 392, const.enemySpritePath, 120)
        enemy_list = pygame.sprite.Group()
        weapon_list = pygame.sprite.Group()
        sword_list = pygame.sprite.Group()
        boss = Boss(0, 0, const.bossSpritePath, 500)
        playerGroup = pygame.sprite.Group()
        playerGroup.add(player)
        blood_font = get_font(20)
        #score
        score = 0
        score_font = get_font(20)
        def display_score():
            score_surface = score_font.render(f'Score:{int(score)}', True, const.white)
            score_rect = score_surface.get_rect(center=(700, 80))
            display.blit(score_surface, score_rect)
        def display_blood():
            blood_surface=blood_font.render(f'Health:{int(player.blood)}', True, const.red_blood)
            blood_rect = blood_surface.get_rect(center=(110, 80))
            display.blit(blood_surface, blood_rect)
        def create_platform():
            rand = random.randint(0, 100)
            platform_y_position=random.choice(platform_height)
            if rand <= 55:
                new_platform = Platform(900, platform_y_position, const.platformSpritePath, False, True, False)
                new_enemy = Enemy(new_platform.rect.centerx, new_platform.rect.top-42, const.enemySpritePath, 120)
                enemy_list.add(new_enemy)
            if rand <=4 or rand >= 96:
                new_platform = Platform(900, platform_y_position, const.platformSpritePath, False, False, True)
                new_weapon = Weapon(new_platform.rect.centerx + 30, new_platform.rect.top-16, const.swordSpritePath, 100)
                weapon_list.add(new_weapon)
            else:
                new_platform = Platform(900, platform_y_position, const.platformSpritePath, False, False, False)
            return new_platform
        def move_platforms(platforms):
            for platform in platforms:
                if platform != firstPlatform:
                    platform.update()
            return platforms
        def move_enemy(enemies):
            for enemy in enemies:
                enemy.rect.x-=2
                enemy.drawEnemy(enemy.rect.x-37, enemy.rect.y, display)
            return enemies
        def move_weapon(weapons):
            for weapon in weapons:
                weapon.rect.x-=2
            return weapons
        def draw_platforms(platforms):
            for platform in platforms:
                if not platform.isFirst and platform.hasEnemy:
                    enemy.drawEnemy(platform.rect.centerx-36, platform.rect.top-42, display)
                    enemy.rect.topleft = (platform.rect.centerx-30, platform.rect.top-42)
                if not platform.isFirst and platform.hasWeapon:
                    sword.drawWeapon(platform.rect.centerx + 30, platform.rect.top-16, display)
                    sword.rect.topleft = (platform.rect.centerx + 30, platform.rect.top-16)
        
                #dagger.drawWeapon(platform.rect.centerx+30, platform.rect.top-16, display)
                display.blit(platform.image, (platform.x, platform.y))

        def checkPlatformCollisionWithPLayer(platforms):
            for platform in platforms:
                if platform.rect.colliderect(player.rect):
                    player.isStanding = True
                    break
                else:
                    player.isStanding = False
                #TODO
                #if platform.x < -200:
                    
        #TODO: change the background

        while not gameOver:
            if player.rect.y > 569:
                ingameSound.stop()
                deathSound.play()
                self.level = 4
                self.finalScore = score
                saveData.saveData("save.txt", leaderboard)
                self.stateManager()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player.animateSelf()
                    for thisEnemy in enemy_list:
                        if player.rect.colliderect(thisEnemy.rect) and not thisEnemy.health <= 0:
                            print("bruhhhhhhhhh")
                            thisEnemy.takeDamage(player)
                            if player.blood < 100:
                                player.blood += 6
                            score += 10
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
                    if event.key == pygame.K_d:
                        player.rightPressed = True
                    if event.key == pygame.K_SPACE:
                        player.jumpPressed = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.level = 1
                            ingameSound.stop()
                            saveData.saveData("save.txt", leaderboard)
                            self.stateManager()
                #KEYUP EVENTS
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player.leftPressed = False
                    if event.key == pygame.K_d:
                        player.rightPressed = False
                    if event.key == pygame.K_SPACE:
                        player.jumpPressed = False

                if player.rect.colliderect(testTrigger.rect):
                    testTrigger.action()

            for thisEnemy in enemy_list:
                if thisEnemy.rect.colliderect(player.rect) and not thisEnemy.isAnimating:
                    player.blood -= 0.1
            for thisWeapon in weapon_list:
                if player.rect.colliderect(thisWeapon):
                    player.animationDos()
                    player.weapon = sword
            player.update()
            enemy.update()
            player.updateSprite()
            enemy.updateSprite()
            if player.blood <= 0:
                ingameSound.stop()
                deathSound.play()
                self.level = 4
                self.finalScore = score
                self.stateManager()
            player.rect.centery += const.playerMovement
            display.blit(bgScaled, (0, 0))

            checkPlatformCollisionWithPLayer(platform_list)

            display.blit(player.image,(player.rect.x, player.rect.y))
            #display.blit(boss.image, (boss.rect.x, boss.rect.y))
            display_score()
            player.blood -= 0.08
            score += 0.04
            #platform_list = move_platforms(platform_list) 
            platform_list.update()
            draw_platforms(platform_list)
            enemy_list = move_enemy(enemy_list)
            weapon_list = move_weapon(weapon_list)
            #draw_enemy(enemy_list)
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
        if self.level == 4:
            self.game_Over()
            
            

#innit
pygame.mixer.pre_init(frequency = 20000, size = 16, channels = 1, buffer = 256)
pygame.init()
deathSound = pygame.mixer.Sound("Audio/Death.wav")
mainMenuSound = pygame.mixer.Sound("Audio/MainMenu.wav")
ingameSound = pygame.mixer.Sound("Audio/ingame.wav")
deathSound.set_volume(0.5)
mainMenuSound.set_volume(0.06)
ingameSound.set_volume(0.035)
display = pygame.display.set_mode((const.disW, const.disH))
pygame.display.set_caption(const.gameName)
clock = pygame.time.Clock()
     
stateManager = StateManager()
    
#gameloop
def gameLoop():
    while True:
        stateManager.stateManager()

gameLoop()

