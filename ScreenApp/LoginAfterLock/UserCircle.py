import pygame.sprite
from pygame.locals import (
RLEACCEL
)
from constant import (
SCREENWIDTH,
SCREENHEIGHT
)




class UserCircle(pygame.sprite.Sprite):
    def __init__(self):
        super(UserCircle, self).__init__()
        self.surf = pygame.image.load("ScreenApp/LoginAfterLock/Assets/profile_icon_login.png").convert()
        self.surf = pygame.transform.scale(self.surf, (200, 200))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(SCREENWIDTH / 2, SCREENHEIGHT / 2 -100)
        )
