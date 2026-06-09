import math

import pygame
from constant import (
    SCREENWIDTH,
    SCREENHEIGHT
)


class LoadingCircle(pygame.sprite.Sprite):
    def __init__(self):
        super(LoadingCircle, self).__init__()
        self.surf = pygame.Surface((50, 50), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(
            center=(SCREENWIDTH / 2, SCREENHEIGHT / 2 + 200)

        )
        self.angle = 0
        self.radius = 25
        self.borderWidth = 3
        self.color = (255, 255, 255)
        self.active = True
        #circumfrenced of a circle is the length of line to drow a circle
        #formular for circle cir circumference is 2 x pi x r
        #pi constant is 3.14159
        self.arcLength = math.pi / 2

        self.startingtime = pygame.time.get_ticks()
        self.stopupdate = False

    def update(self):
        currenttime = pygame.time.get_ticks()
        if currenttime - self.startingtime > 6000:
            self.stopupdate = True
            return
        startAngle = self.angle
        endAngle = self.angle + self.arcLength



        pygame.draw.arc(
            self.surf,
            self.color,
            (0, 0, 50, 50),
            startAngle,
            endAngle,
            self.borderWidth
        )

        self.angle += 0.01

        if self.angle > math.tau:
            self.angle -= math.tau
            self.active = not self.active

        if not self.active:
            self.color = (0, 0, 0)
        else:
            self.color = (255, 255, 255)
