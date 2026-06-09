import pygame
from pygame import K_ESCAPE

from constant import SystemStateEnum
from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
    K_SPACE,
    QUIT,
    MOUSEBUTTONDOWN
)
import constant

#inishalise pygame
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
constant.SCREENWIDTH, constant.SCREENHEIGHT = screen.get_size()

#startuup screen imports
from ScreenApp.LoadingScreenAtStartup.DrawWindowsLOgoSprite import DrawWindowsLogo
from ScreenApp.LoadingScreenAtStartup.LodingCIrcleSPrite import LoadingCircle
#lock screen imports
from ScreenApp.lockScreen.LockClockSprite import ClockSprite
from ScreenApp.lockScreen.DateSprite import DateSprite
#login after startup imports
from ScreenApp.LoginAfterLock.UserCircle import UserCircle
from ScreenApp.LoginAfterLock.PasswordTextbox import PasswordInputSprite
#Home SCreen
from ScreenApp.MainHomeScreen.TaskBar import TaskBarSprite
#program imports
from AppProgram.WinStart.Button import WinButton
from AppProgram.fileExplore.button import FileExplorerB
from AppProgram.WinStart.WindowsSMenu.menu import thePopup

#sprite grope
ButtonWindows = WinButton()

Explorerf = FileExplorerB()
taskbar_sprites = pygame.sprite.Group()
taskbar_sprites.add(ButtonWindows, Explorerf)

#sprites for startup loading screen
windowslogo = DrawWindowsLogo()
loadingcircle = LoadingCircle()
Sturtup_Loading_Sprites = pygame.sprite.Group()
Sturtup_Loading_Sprites.add(windowslogo, loadingcircle)

#Sprite blob for locky screen
lcc = ClockSprite()
ds = DateSprite()

lock_sprites = pygame.sprite.Group()
lock_sprites.add(lcc, ds)
#sprrite login to main windows login
usrico = UserCircle()
passtextbox = PasswordInputSprite()
main_login_sprites = pygame.sprite.Group()
main_login_sprites.add(usrico, passtextbox)
#sprites for the main home screen
TaskBarHome = TaskBarSprite(taskbar_sprites)
WinMenuStart = thePopup()

main_home_sprites = pygame.sprite.Group()
main_home_sprites.add(TaskBarHome)

#systemy staty
# current_state = SystemStateEnum.STURTUPLOADINGSCREEN
current_state = SystemStateEnum.WINDOWSHOMESCREEN

#backgrnd images
lock_screen_background = pygame.image.load("globasset/lockbacko.jpg").convert()
lock_screen_background = pygame.transform.scale(lock_screen_background, (constant.SCREENWIDTH, constant.SCREENHEIGHT))
blur_intensity = 0.2
compressed = pygame.transform.smoothscale(lock_screen_background, (int(constant.SCREENWIDTH * blur_intensity),
                                                                   int(constant.SCREENHEIGHT * blur_intensity)))
login_backs = pygame.transform.scale(compressed, (constant.SCREENWIDTH, constant.SCREENHEIGHT))

home_background = pygame.image.load("globasset/WindowsHomeScreen.jpg").convert()
home_background = pygame.transform.scale(home_background, (constant.SCREENWIDTH, constant.SCREENHEIGHT))
#gamelloop
running = True
while running:
    screen.fill((0, 0, 0))

    #event loop
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_SPACE and current_state == SystemStateEnum.LOCKAFTERSTARTUP:
                current_state = SystemStateEnum.LOGINTOWINDOWS
        if event.type == QUIT:
            running = False

        if current_state == SystemStateEnum.LOGINTOWINDOWS:
            passwordCheck = passtextbox.handleTypeEvent(event)
            passtextbox.handleClickEvent(event)
            if passwordCheck:
                current_state = SystemStateEnum.WINDOWSHOMESCREEN
        if current_state == SystemStateEnum.WINDOWSHOMESCREEN:
            if event.type == MOUSEBUTTONDOWN:
                if ButtonWindows.handleClickEvent(event, TaskBarHome.rect):
                    WinMenuStart.active = not WinMenuStart.active
                elif WinMenuStart.active:
                    if not WinMenuStart.rect.collidepoint(event.pos):
                        WinMenuStart.active = False
    if current_state == SystemStateEnum.STURTUPLOADINGSCREEN:
        #sprite update
        Sturtup_Loading_Sprites.update()
        #render sprite
        for entity in Sturtup_Loading_Sprites:
            screen.blit(entity.surf, entity.rect)

        if loadingcircle.stopupdate:
            current_state = SystemStateEnum.LOCKAFTERSTARTUP
    if current_state == SystemStateEnum.LOCKAFTERSTARTUP:
        screen.blit(lock_screen_background, (0, 0))
        lock_sprites.update()

        for entity in lock_sprites:
            screen.blit(entity.surf, entity.rect)
    if current_state == SystemStateEnum.LOGINTOWINDOWS:
        screen.blit(login_backs, (0, 0))
        dark_overlay = pygame.Surface((constant.SCREENWIDTH, constant.SCREENHEIGHT))
        dark_overlay.fill((0, 0, 0))
        dark_overlay.set_alpha(180)
        screen.blit(dark_overlay, (0, 0))
        main_login_sprites.update()
        for entity in main_login_sprites:
            screen.blit(entity.surf, entity.rect)
    elif current_state == SystemStateEnum.WINDOWSHOMESCREEN:
        screen.blit(home_background, (0, 0))
        main_home_sprites.update()
        for entity in main_home_sprites:
            screen.blit(entity.surf, entity.rect)

        if WinMenuStart.active:
            screen.blit(WinMenuStart.surf, WinMenuStart.rect)
    pygame.display.flip()
