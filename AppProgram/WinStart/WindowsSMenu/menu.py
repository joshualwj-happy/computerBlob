import pygame
from pygame import RLEACCEL
from constant import(
SCREENWIDTH,
SCREENHEIGHT
)

from AppProgram.WinStart.WindowsSMenu.WindowsFottrStrt import theFooter


class thePopup(pygame.sprite.Sprite):
        def __init__(self):
            super(thePopup, self).__init__()
            width1 = SCREENWIDTH - 650
            height1 = SCREENHEIGHT - 100
            self.surf = pygame.Surface((width1, height1), pygame.SRCALPHA)
            self.surf.fill((0, 0, 0, 0))
            pygame.draw.rect(
                self.surf,
                (30, 30, 30, 230),
                (0, 0, width1, height1),
                border_radius=30

            )

            self.rect = self.surf.get_rect(
                midbottom=(SCREENWIDTH / 2, SCREENHEIGHT - 65)

            )
            self.active = False

            self.footer = theFooter()


            self.update()

        def update(self):
            self.footer.update()
            width1 = SCREENWIDTH - 650
            height1 = SCREENHEIGHT - 100
            footer_rect = self.footer.surf.get_rect(
                midbottom=(width1 / 2, height1)
            )
            self.surf.blit(self.footer.surf, footer_rect)