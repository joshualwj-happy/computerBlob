import pygame
from pygame import RLEACCEL
from constant import(
SCREENWIDTH,
SCREENHEIGHT
)

from AppProgram.WinStart.WindowsSMenu.UsrIcoBtn import WinUsrIco
from AppProgram.WinStart.WindowsSMenu.WinUsrGrp import theGroup

class theFooter(pygame.sprite.Sprite):
    def __init__(self):
        super(theFooter, self).__init__()
        width1 = SCREENWIDTH - 650
        height1 = SCREENHEIGHT - 730
        self.surf = pygame.Surface((width1, height1), pygame.SRCALPHA)
        self.surf.fill((255, 0, 0, 0))
        pygame.draw.rect(
            self.surf,
            (10, 10, 10),
            (0, 0, width1, height1),
            border_bottom_right_radius=25,
            border_bottom_left_radius=25

        )

        self.rect = self.surf.get_rect(
            midbottom=(SCREENWIDTH / 2, SCREENHEIGHT - 90)
        )

        #wswwswswswswsws

        self.theGroup = theGroup()

        theGroup_rect = self.theGroup.surf.get_rect(
            midleft=(50, height1 / 2)
        )
        self.surf.blit(self.theGroup.surf, theGroup_rect)