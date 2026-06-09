import datetime

import pygame.sprite

from constant import (
    SCREENWIDTH,
    SCREENHEIGHT
)


class DateSprite(pygame.sprite.Sprite):
    def __init__(self, ):
        super(DateSprite, self).__init__()
        self.surf = pygame.Surface((800, 200), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(
            center=(SCREENWIDTH / 2, SCREENHEIGHT / 2 -80)
        )
        self.font = pygame.font.SysFont(None, 30)
        self.update()

    def update(self):
        self.surf.fill((0, 0, 0, 0))

        todayd = datetime.datetime.now().strftime("%A, %#d %B %Y")
        datetext = self.font.render(todayd, True, (255, 255, 255))
        datetext_rect = datetext.get_rect(
            center=(self.surf.get_width() / 2, self.surf.get_height() / 2)
        )
        self.surf.blit(datetext, datetext_rect)
