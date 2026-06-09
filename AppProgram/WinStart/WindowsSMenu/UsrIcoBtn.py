import pygame
from pygame import RLEACCEL
from constant import(
SCREENWIDTH,
SCREENHEIGHT
)

class WinUsrIco(pygame.sprite.Sprite):
    def __init__(self):
        super(WinUsrIco)
        self.surf = pygame.image.load('AppProgram/WinStart/assest/teamsPeople.png ')
        self.surf = pygame.transform.scale(self.surf, (60, 55))
