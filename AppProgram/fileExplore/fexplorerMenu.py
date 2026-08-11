import pygame

from constant import (
    SCREENWIDTH,
    SCREENHEIGHT
)
from AppProgram.Utility.UniversalTBar import UTB

class FexplorerPopup(pygame.sprite.Sprite):
        def __init__(self):
            super(FexplorerPopup, self).__init__()
            self.width1 = SCREENWIDTH - 400
            self.height1 = SCREENHEIGHT - 200
            self.surf = pygame.Surface((self.width1, self.height1), pygame.SRCALPHA)
            self.surf.fill((0, 0, 0, 0))
            pygame.draw.rect(
                self.surf,
                (30, 30, 30, 255),
                (0, 0, self.width1, self.height1),
                border_radius=0

            )

            self.rect = self.surf.get_rect(
                midbottom=(SCREENWIDTH / 2, SCREENHEIGHT - 65)

            )
            self.active = False

            self.TopMenu = UTB(self.width1)
            self.update()

        def update(self):
            self.surf.fill((0, 0, 0, 0, ))
            pygame.draw.rect(
                self.surf,
                (20, 20, 20, 255),
                (0, 0, self.width1, self.height1)

            )

            self.surf.blit(self.TopMenu.surf, (0, 0))
