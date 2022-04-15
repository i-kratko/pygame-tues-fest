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
from health import Health
from random import randint
from platform import Platform

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Graphics/font.ttf", size)

score = 0
name = "BRUH"

leaderboard = {
    'firstPlaceName' : "SUS",
    'firstPlaceScore' : 30,
    'secondPlaceName' : "SUSSIA",
    'secondPlaceScore' : 21,
    'thirdPlaceName' : "KLENDI",
    'thirdPlaceScore' : 15,
    'fourthPlaceName' : "4e6ma",
    'fourthPlaceScore' : 10,
    'fifthPlaceName' : "bancig",
    'fifthPlaceScore' : 1
}

leaderboard = saveData.loadData("Code\save.txt")

#bruh
class StateManager():

    def __init__(self):
        self.level = 1
        self.finalScore = 1

    def leaderboard(self):
        gameOver = False

        bgSurface = pygame.Surface((800,600))
        bgSurface.fill('Black')

        LEADERBOARD = get_font(69).render("LEADERBOARD", True, "#ffffff")
        FIRST_PLACE = get_font(30).render(f'#1 {leaderboard["firstPlaceName"]} {leaderboard["firstPlaceScore"]}', True, "#8a87b3")
        FIRST_PLACE_RECT = FIRST_PLACE.get_rect()
        FIRST_PLACE_RECT.centerx = const.disW / 2
        SECOND_PLACE = get_font(30).render(f'#2 {leaderboard["secondPlaceName"]} {leaderboard["secondPlaceScore"]}', True, "#c0fad0")
        SECOND_PLACE_RECT = SECOND_PLACE.get_rect()
        SECOND_PLACE_RECT.centerx = const.disW / 2
        THIRD_PLACE = get_font(30).render(f'#3 {leaderboard["thirdPlaceName"]} {leaderboard["thirdPlaceScore"]}', True, "#f7e57c")
        THIRD_PLACE_RECT = THIRD_PLACE.get_rect()
        THIRD_PLACE_RECT.centerx = const.disW / 2
        FOURTH_PLACE = get_font(30).render(f'#4 {leaderboard["fourthPlaceName"]} {leaderboard["fourthPlaceScore"]}', True, "#bcbdb9")
        FOURTH_PLACE_RECT = FOURTH_PLACE.get_rect()
        FOURTH_PLACE_RECT.centerx = const.disW / 2
        FIFTH_PLACE = get_font(30).render(f'#5 {leaderboard["fifthPlaceName"]} {leaderboard["fourthPlaceScore"]}', True, "#7d5f40")
        FIFTH_PLACE_RECT = FIFTH_PLACE.get_rect()
        FIFTH_PLACE_RECT.centerx = const.disW / 2
        BACK_BUTTON = Button(280, 450, const.backButtonPath)

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
            display.blit(LEADERBOARD, (25, 33))
            display.blit(FIRST_PLACE, (FIRST_PLACE_RECT.x, 130))
            display.blit(SECOND_PLACE, (SECOND_PLACE_RECT.x, 170))
            display.blit(THIRD_PLACE, (THIRD_PLACE_RECT.x, 210))
            display.blit(FOURTH_PLACE, (FOURTH_PLACE_RECT.x, 250))
            display.blit(FIFTH_PLACE, (FIFTH_PLACE_RECT.x, 290))
            display.blit(BACK_BUTTON.image, (280, 450))
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
        LEADERBOARD_BUTTON = Button(220,280, const.leaderboardButtonPath)
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
                    if LEADERBOARD_BUTTON.rect.collidepoint(pos):
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
            display.blit(LEADERBOARD_BUTTON.image, (95,280))
            display.blit(QUIT_BUTTON.image, (280,410))

            pygame.display.update()
            clock.tick(const.FPS)


    def game_Over(self):
        gameOver = False
        bgSurface = pygame.Surface((800,600))
        bgSurface.fill('Black')
        scoreText = get_font(45).render(f'SCORE: {int(self.finalScore)}', True, "#ffffff")
        gameOver_TEXT = get_font(72).render("GAME OVER", True, "#ffffff")  
        pressButton1 = get_font(20).render("press any key to", True, "#ffffff")  
        pressButton2 = get_font(20).render("continue", True, "#ffffff")  

        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ingameSound.stop()
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    self.level = 5
                    self.stateManager()


            display.blit(bgSurface,(0,0))
            display.blit(scoreText, (170,110))
            display.blit(gameOver_TEXT, (75,220))
            display.blit(pressButton1, (225,420))
            display.blit(pressButton2, (308,455))

            pygame.display.update()
            clock.tick(const.FPS)


    def enterNameScreen(self):
        gameOver = False
        bgSurface = pygame.Surface((800,600))
        bgSurface.fill('Black')
        gameOver_TEXT = get_font(48).render("ENTER YOUR NAME", True, "#ffffff")  
        QUIT_BUTTON = Button(280, 410, const.quitGameOverButtonPath)
        pressButton1 = get_font(20).render("press ENTER key to", True, "#ffffff")  
        pressButton2 = get_font(20).render("continue", True, "#ffffff")  

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
                    if event.key == pygame.K_RETURN:
                        self.level = 1
                        self.stateManager()


            display.blit(bgSurface,(0,0))
            display.blit(gameOver_TEXT, (40,100))
            display.blit(pressButton1, (210,335))
            display.blit(pressButton2, (314,370))
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
        platform_height= [205, 250, 295]
        spawn_platform=pygame.USEREVENT 
        spawn_enemy=pygame.USEREVENT
        pygame.time.set_timer(spawn_platform, const.spawn_platform_time)    
        ##PLAT COUNTER
        self.platformCounter = 0
        #first platfrom
        firstPlatform = Platform(20, 200, const.platformSpritePath, True, False, False)
        platform_list.add(firstPlatform)
        #creating the player
        dagger = Weapon(350,418, const.daggerSpritePath, 30)
        sword = Weapon(350,418, const.swordSpritePath, 20)
        player = Player(40, 100, const.playerSpritePath, 100, dagger)
        enemy = Enemy(500, 392, const.enemySpritePath, 120)
        heart = Health(100,100, const.heartPath, 20, False)
        heart_list = pygame.sprite.Group()
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

        def checkIfRecrod():
            while 1:
                print("AMA VERNO")
                if score > leaderboard["fifthPlaceScore"]:
                    if score > leaderboard["fourthPlaceScore"]:
                        if score > leaderboard["thirdPlaceScore"]:
                            if score > leaderboard["secondPlaceScore"]:
                                if score > leaderboard["firstPlaceScore"]:
                                    #1 place
                                    leaderboard["fifthPlaceScore"] = leaderboard["fourthPlaceScore"]
                                    leaderboard["fifthPlaceName"] = leaderboard["fourthPlaceName"]
                                    leaderboard["fourthPlaceScore"] = leaderboard["thirdPlaceScore"]
                                    leaderboard["fourthPlaceName"] = leaderboard["thirdPlaceName"]
                                    leaderboard["thirdPlaceScore"] = leaderboard["secondPlaceScore"]
                                    leaderboard["thirdPlaceName"] = leaderboard["secondPlaceName"]
                                    leaderboard["secondPlaceScore"] = leaderboard["firstPlaceScore"]
                                    leaderboard["secondPlaceName"] = leaderboard["firstPlaceName"]
                                    leaderboard["firstPlaceScore"] = int(score)
                                    leaderboard["firstPlaceName"] = name
                                    break
                                #2 place
                                leaderboard["fifthPlaceScore"] = leaderboard["fourthPlaceScore"]
                                leaderboard["fifthPlaceName"] = leaderboard["fourthPlaceName"]
                                leaderboard["fourthPlaceScore"] = leaderboard["thirdPlaceScore"]
                                leaderboard["fourthPlaceName"] = leaderboard["thirdPlaceName"]
                                leaderboard["thirdPlaceScore"] = leaderboard["secondPlaceScore"]
                                leaderboard["thirdPlaceName"] = leaderboard["secondPlaceName"]
                                leaderboard["secondPlaceScore"] = int(score)
                                leaderboard["secondPlaceName"] = name
                                break
                            #3 place
                            leaderboard["fifthPlaceScore"] = leaderboard["fourthPlaceScore"]
                            leaderboard["fifthPlaceName"] = leaderboard["fourthPlaceName"]
                            leaderboard["fourthPlaceScore"] = leaderboard["thirdPlaceScore"]
                            leaderboard["fourthPlaceName"] = leaderboard["thirdPlaceName"]
                            leaderboard["thirdPlaceScore"] = int(score)
                            leaderboard["thirdPlaceName"] = name
                            break

                        #4 place
                        leaderboard["fifthPlaceScore"] = leaderboard["fourthPlaceScore"]
                        leaderboard["fifthPlaceName"] = leaderboard["fourthPlaceName"]
                        leaderboard["fourthPlaceScore"] = int(score)
                        leaderboard["fourthPlaceName"] = name
                        break
                    #5 place
                    leaderboard["fifthPlaceScore"] = int(score)
                    leaderboard["fifthPlaceName"] = name
                    break
                break

        while not gameOver:
            if player.rect.y > 569:
                ingameSound.stop()
                deathSound.play()
                self.level = 4
                self.finalScore = score
                checkIfRecrod()
                saveData.saveData("Code\save.txt", leaderboard)
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
                            if thisEnemy.health <= 0:
                                heart.heartPicked = True
                            if player.blood < 100:
                                player.blood += 6
                            score += 10
                            heart.heartPicked = False
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
                saveData.saveData("Code\save.txt", leaderboard)
                checkIfRecrod()
                self.stateManager()
            player.rect.centery += const.playerMovement
            display.blit(bgScaled, (0, 0))

            if heart.heartPicked == True:
                display.blit (heart.image, (thisEnemy.x + 20, thisEnemy.y))

            checkPlatformCollisionWithPLayer(platform_list)

            display.blit(player.image,(player.rect.x, player.rect.y))
            #display.blit(boss.image, (boss.rect.x, boss.rect.y))
            display_score()
            if score > 14:
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
            self.leaderboard()
        if self.level == 4:
            self.game_Over()
        if self.level == 5:
            self.enterNameScreen()
            
            

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

