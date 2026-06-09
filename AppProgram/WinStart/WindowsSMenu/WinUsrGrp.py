import pygame
from pygame import RLEACCEL
from constant import(
SCREENWIDTH,
SCREENHEIGHT
)

from AppProgram.WinStart.WindowsSMenu.UsrIcoBtn import WinUsrIco
from AppProgram.WinStart.WindowsSMenu.UserTxt import UsrNme

class theGroup(pygame.sprite.Sprite):
    def __init__(self):
        super(theGroup, self).__init__()
        width1 = 200
        height1 = 50
        self.surf = pygame.Surface((width1, height1), pygame.SRCALPHA)
        self.surf.fill((255, 0, 0, 0))

        self.default_color = (10, 10, 10, 230)
        self.hover_color = (200, 200, 200, 230)
        pygame.draw.rect(
            self.surf,
            self.default_color,
            (0, 0, width1, height1),
            border_radius=10,


        )

        self.rect = self.surf.get_rect(
            midbottom=(SCREENWIDTH / 2, SCREENHEIGHT - 90)


        )

        self.userIco = WinUsrIco()

        userIco_rect = self.userIco.surf.get_rect(
            midleft=(10, height1 / 2)
        )


        #
        self.surf.blit(self.userIco.surf, userIco_rect)

        self.userNme = UsrNme()

        userNme_rect = self.userNme.surf.get_rect(
            midleft=(70, height1 / 2)
        )
        self.surf.blit(self.userNme.surf, userNme_rect)

    def draw_background(self, color):
        width, height = self.surf.get_size()
        self.surf.fill((0, 0, 0, 0))
        pygame.draw.rect(
            self.surf,
            color,
            (0, 0, width, height),
            border_radius=5
        )

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            self.draw_background(self.hover_color)

        else:
            self.draw_background(self.default_color)

        self.render_children()

    def render_children(self):
        width, height = self.surf.get_size()

        userIco_rect = self.userIco.surf.get_rect(
            midleft=(10, height / 2)
        )


        #
        self.surf.blit(self.userIco.surf, userIco_rect)

        userNme_rect = self.userNme.surf.get_rect(
            midleft=(70, height / 2)
        )
        self.surf.blit(self.userNme.surf, userNme_rect)
