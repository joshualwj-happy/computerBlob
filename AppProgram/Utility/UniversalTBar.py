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

        self.closeButton = CloseBSprite()
        self.minimizeButton = MinimizeBSprite()
        self.fullSButton = FullSBSprite()
