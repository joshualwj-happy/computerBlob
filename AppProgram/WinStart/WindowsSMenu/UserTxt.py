import pygame
from pygame import RLEACCEL
from constant import(
SCREENWIDTH,
SCREENHEIGHT
)

class UsrNme(pygame.sprite.Sprite):
    def __init__(self):
        super(UsrNme, self).__init__()
        self.surf = pygame.Surface((200, 80), pygame.SRCALPHA)
        self.font = pygame.font.SysFont(None, 25)
        self.update()

    def update(self):
        self.surf.fill((0, 0, 0, 0))

        username = 'Josh Blob'

        text = self.font.render(username, True, (255, 255, 255))

        text_rect = text.get_rect(
            midleft=(0, self.surf.get_height() / 2)
        )
        self.surf.blit(text, text_rect)