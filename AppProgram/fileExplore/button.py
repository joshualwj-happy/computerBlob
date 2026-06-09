import pygame
from pygame import RLEACCEL
from constant import(
SCREENWIDTH,
SCREENHEIGHT
)

class FileExplorerB(pygame.sprite.Sprite):
    def __init__(self):
        super(FileExplorerB, self).__init__()
        self.surf = pygame.image.load('AppProgram/fileExplore/Assest/fexplorer.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (45, 45))
        self.rect = self.surf.get_rect(
            midleft=(SCREENWIDTH / 2 - 143, 30)

        )