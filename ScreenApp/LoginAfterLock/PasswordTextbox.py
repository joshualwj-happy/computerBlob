import pygame.sprite
from constant import (
SCREENWIDTH,
SCREENHEIGHT
)
from user import WindowsUser
import userState


class PasswordInputSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(PasswordInputSprite, self).__init__()
        self.surf = pygame.Surface((250, 35))
        self.rect = self.surf.get_rect(
            center=(SCREENWIDTH / 2, SCREENHEIGHT / 2 +50)
        )
        self.font = pygame.font.SysFont(None, 24)
        self.active = False
        self.placeholder = 'Enter your password'
        self.color_active = pygame.Color('#3399FF')
        self.color_inactive = pygame.Color('gray')
        self.color = self.color_inactive
        self.text = ''
        self.eye_open = pygame.image.load('ScreenApp/LoginAfterLock/Assets/open.png')
        self.eye_close = pygame.image.load('ScreenApp/LoginAfterLock/Assets/close.png')
        self.eye_open = pygame.transform.scale(self.eye_open, (25, 16))
        self.eye_close = pygame.transform.scale(self.eye_close, (25, 16))
        self.eye_rect = self.eye_close.get_rect()
        self.eye_rect.right = self.surf.get_width() - 10
        self.eye_rect.centery = self.surf.get_height() // 2
        self.eye_open.get_rect()
        self.show_password = False
    def update(self):
        self.surf.fill((255, 255, 255))

        pygame.draw.rect(self.surf, self.color, self.rect, 10)

        if not self.active and self.text == '':
            display_text = self.placeholder
            text_colour = (150,150,150)
        else:
            if self.show_password:
                display_text = self.text
            else:
                display_text = "•" * len(self.text)
            text_colour = (0, 0, 0)

        text_surf = self.font.render(display_text, True, text_colour)
        self.surf.blit(text_surf,(10,(35 - text_surf.get_height()) // 2))
        eye_icon = self.eye_open if self.show_password else self.eye_close
        self.surf.blit(eye_icon, self.eye_rect)

    def handleTypeEvent(self, event):
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                user = self.getUserCredentiels()
                userPassword = user.password
                return userPassword == self.text
            else:
                self.text += event.unicode

    def handleClickEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            local_pos = (
                event.pos[0] - self.rect.x,
                event.pos[1] - self.rect.y
            )
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = self.color_active
            else:
                self.active = False
                self.color = self.color_inactive
            if self.eye_rect.collidepoint(local_pos):
                self.show_password = not self.show_password
                return



    def getUserCredentiels(self):
        credentielFile = open("DataBase/Credentiels.txt", "r")
        userCredentiels = credentielFile.readlines()
        userInfo = userCredentiels[0]
        username, userId, password = userInfo.split("|")
        user = WindowsUser(userId, username, password)
        userState.currentUser = user
        return user