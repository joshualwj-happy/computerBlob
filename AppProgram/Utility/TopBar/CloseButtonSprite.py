import pygame

class CloseBSprite():
    def __init__(self, height):
        super(CloseBSprite, self).__init__
        self.surf = pygame.image.load('AppProgram/Utility/TopBar/assest/closeButton.png').convert()
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        