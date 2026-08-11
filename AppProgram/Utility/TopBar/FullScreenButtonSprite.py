import pygame

class FullSBSprite():
    def __init__(self, height):
        super(FullSBSprite, self).__init__
        self.surf = pygame.image.load('AppProgram/Utility/TopBar/assest/fullScreenButton.png').convert()
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        