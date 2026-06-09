import datetime

from constant import (
SCREENWIDTH,
SCREENHEIGHT
)
import pygame.sprite




class ClockSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(ClockSprite, self).__init__()
        self.surf = pygame.Surface((970, 530), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(
            center=(SCREENWIDTH/2, SCREENHEIGHT/2 - 130)

        )
        self.font = pygame.font.SysFont(None, 150)
        self.update()
    def update(self):
        self.surf.fill((0, 0, 0, 0))
        timeNow = datetime.datetime.now().strftime("%H:%M")
        textTime = self.font.render(timeNow, True, (255, 255, 255))
        textRect = textTime.get_rect(
            center=(self.surf.get_width() / 2, self.surf.get_height()/ 2)
        )
        self.surf.blit(textTime, textRect)