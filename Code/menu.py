from ast import While
from tkinter import font
import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect


BLUE = (106, 159, 181)
WHITE = (255, 255, 255)

def create_surfaceText(text, fontSize, text_Colour, backGr_Colour):
    font = pygame.freetype.SysFont("Times New Roman", fontSize, bold = True)
    surface, _ = font.render(text = text, fgcolor = text_Colour, bgcolor = backGr_Colour)
    return surface.convert_alpha()


class UI_Element(Sprite):
    
    def __init__(self, centerPos, text, fontSize, backGr_Colour, text_Colour):
        self.mouse_over = False

        super().__init__()

        default_image = create_surfaceText(text, fontSize, text_Colour, backGr_Colour)

        over_image = create_surfaceText(text, fontSize * 1.2, text_Colour, backGr_Colour)

        self.images = [default_image, over_image]
        self.rects = [default_image.get_rect(center = centerPos), over_image.get_rect(center = centerPos)]

    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]
    
    def update(self, mousePos):
        if self.rect.collidepoint(mousePos):
            self.mouse_over = True
        else:
            self.mouse_over = False
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)


def main():
    pygame.init()

    screen = pygame.display.set_mode((500,300))

    uielement = UI_Element(centerPos = (150,150), fontSize = 30, backGr_Colour = BLUE, text_Colour = WHITE, text = 'Alooooooo')

    while True:
        for event in pygame.event.get():
            pass 
        screen.fill(BLUE)

        uielement.update(pygame.mouse.get_pos())
        uielement.draw(screen)
        pygame.display.filp()


main()