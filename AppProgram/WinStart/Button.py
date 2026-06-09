import pygame

from constant import (
SCREENWIDTH,
SCREENHEIGHT
)

class WinButton(pygame.sprite.Sprite):
    def __init__(self):
        super(WinButton, self).__init__()
        self.surf = pygame.image.load('AppProgram/WinStart/assest/Win11Logo.png').convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (40, 40))
        self.rect = self.surf.get_rect(
            midleft=(SCREENWIDTH / 2 - 200, 30)

        )
    def handleClickEvent(self, event, parent_rect):
        if event.type == pygame.MOUSEBUTTONDOWN:
            local_pos = (
                event.pos[0] - parent_rect.x,
                event.pos[1] - parent_rect.y
            )

            if self.rect.collidepoint(local_pos):
                return True

        return False

