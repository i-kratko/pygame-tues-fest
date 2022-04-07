import pygame
import const

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Graphics/font.ttf", size)

score = 0
score_font = get_font(20)

def display_score(screen):
    score_surface = score_font.render(f'Score:{int(score)}', True, const.white)
    score_rect = score_surface.get_rect(center=(700, 80))
    screen.blit(score_surface, score_rect)