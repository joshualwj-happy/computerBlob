import pygame

class CloseBSprite():
    def __init__(self, height, UTB):
        super(CloseBSprite, self).__init__()
        self.topbar = UTB
        self.surf = pygame.image.load('AppProgram/Utility/TopBar/assest/closeButton.png').convert()
        self.surf = pygame.transform.scale(self.surf, (50, 40))
        self.rect = self.surf.get_rect(
             midright=(self.topbar.width - 10, height / 2)
        )

    def handleClickEvent(self, event, parent_rect):
            if event.type == pygame.MOUSEBUTTONDOWN:
                local_pos = (
                    event.pos[0] - parent_rect.x,
                    event.pos[1] - parent_rect.y
                )
    
                if self.rect.collidepoint(local_pos):
                    self.topbar.active = 0
                    return True