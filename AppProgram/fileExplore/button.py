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

    def handleClickEvent(self, event, parent_rect):
        if event.type == pygame.MOUSEBUTTONDOWN:
            local_pos = (
                event.pos[0] - parent_rect.x,
                event.pos[1] - parent_rect.y
            )

            if self.rect.collidepoint(local_pos):
                return True

        return False