import pygame

class MinimizeBSprite():
    def __init__(self, height):
        super(MinimizeBSprite, self).__init__
        self.surf = pygame.image.load('AppProgram/Utility/TopBar/assest/minimizeButton.png').convert()
        self.surf = pygame.transform.scale(self.surf, (50, 40))
        