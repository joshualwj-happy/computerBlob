import pygame
from pygame import RLEACCEL
from constant import(
SCREENWIDTH,
SCREENHEIGHT
)

class DrawWindowsLogo(pygame.sprite.Sprite):
    def __init__(self):
        super(DrawWindowsLogo, self).__init__()
        self.surf = pygame.image.load('ScreenApp/LoadingScreenAtStartup/assests/w11-removebg-preview.png').convert()
        self.surf = pygame.transform.scale(self.surf,(400, 320))
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(SCREENWIDTH/2, SCREENHEIGHT/2)
        )

