import pygame.sprite
from constant import (
    SCREENWIDTH,
    SCREENHEIGHT
)
class TaskBarSprite(pygame.sprite.Sprite):
    def __init__(self, taskbarPrograms):
        super(TaskBarSprite, self).__init__()

        #Trans Parent
        self.surf = pygame.Surface((SCREENWIDTH, 110))
        self.surf.set_alpha(210)
        self.surf.fill((48 ,48, 48))
        self.rect = self.surf.get_rect(
            center=(SCREENWIDTH / 2, SCREENHEIGHT)
        )
        self.children = taskbarPrograms

    def update(self):
        self.surf.fill((48,48,48))

        for entity in self.children:
            self.surf.blit(entity.surf, entity.rect)


