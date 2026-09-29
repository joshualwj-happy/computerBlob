import pygame
from AppProgram.Utility.TopBar.CloseButtonSprite import CloseBSprite
from AppProgram.Utility.TopBar.FullScreenButtonSprite import FullSBSprite
from AppProgram.Utility.TopBar.MinimizeButtonSprite import MinimizeBSprite
class UTB(pygame.sprite.Sprite):
    def __init__(self, width):
        super(UTB, self).__init__()

        self.height = 45
        self.width = width

        self.surf = pygame.Surface((self.width, self.height), pygame.SRCALPHA)

        self.surf.fill((0, 0, 0, 0))

        pygame.draw.rect(
            self.surf,
            (0, 0, 0, 255),
            (0, 0, self.width, self.height),
            border_radius=0
        )

        self.active = 1

        self.closeButton = CloseBSprite(self.height, self)
        self.minimizeButton = MinimizeBSprite(self.height)
        self.fullSButton = FullSBSprite(self.height)
        
        closebutton_rect = self.closeButton.surf.get_rect(
            midright=(self.width - 15, self.height / 2)
        )
        self.surf.blit(self.closeButton.surf, closebutton_rect)

        minimizebutton_rect = self.minimizeButton.surf.get_rect(
            midright=(self.width - 70, self.height / 2)
        )
        self.surf.blit(self.minimizeButton.surf, minimizebutton_rect)

        fullscreenbutton_rect = self.fullSButton.surf.get_rect(
            midright=(self.width - 125, self.height / 2)
        )
        self.surf.blit(self.fullSButton.surf, fullscreenbutton_rect)
        
        
                

    