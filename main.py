import pygame
from pygame import mixer

from classes import Player, Background, Cursor, Weapon
from config import *
from constants import *

def main():

    # Init program
    pygame.init()
    mixer.init()

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(WINDOW_TITLE)

    # Window icon
    windowIcon = pygame.image.load(WINDOW_ICON_PATH)
    windowIcon = pygame.transform.scale(windowIcon, (32, 32))
    pygame.display.set_icon(windowIcon)

    # Set background
    background = Background(window, BACKGROUND_IMAGE_PATH)
    background.resize(WIDTH, HEIGHT)
    background.setBackground()

    # Init player
    player = Player(window, PLAYER_IMAGE_PATH, int(WIDTH / 2), int(HEIGHT / 2))
    player.resizePlayerImg(
        int(player.playerImg.get_width() * 0.1),
        int(player.playerImg.get_height() * 0.1)
    )

    # Init cursor
    cursor = Cursor(window, CURSOR_IMAGE_PATH)
    cursor.displayCursor()

    weapon = Weapon(window, 'GunMagnum')

    borderX = WIDTH - player.playerImgWidth
    borderY = HEIGHT - player.playerImgHeight

    run = True
    while (run):
        
        dt = clock.tick(60)

        for event in pygame.event.get():
            # Break loop
            if (event.type == pygame.QUIT):
                run = False

            # Mouse button pressed
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                
                # LEFT
                if (event.button == 1):
                    # print('LEFT Mouse DOWN')
                    mouseX, mouseY = pygame.mouse.get_pos()
                    weapon.fire(
                        player.playerX, player.playerY,
                        mouseX, mouseY
                    )

                elif (event.button == 3):
                    # print('RIGHT Mouse DOWN')
                    pass

        # Get key pressed by user / player
        keys = pygame.key.get_pressed()

        dx, dy = 0, 0

        # W
        if (keys[pygame.K_w]):
            # print('W')
            dy = -1 * PLAYER_MAX_MOVE_SPEED_NORMAL * dt
        
        # A
        if (keys[pygame.K_a]):
            # print('A')
            dx = -1 * PLAYER_MAX_MOVE_SPEED_NORMAL * dt
        
        # S
        if (keys[pygame.K_s]):
            # print('S')
            dy = PLAYER_MAX_MOVE_SPEED_NORMAL * dt
        
        # D
        if (keys[pygame.K_d]):
            # print('D')
            dx = PLAYER_MAX_MOVE_SPEED_NORMAL * dt
        
        player.playerX += dx
        player.playerY += dy

        if (player.playerX <= 0):
            player.playerX = 0
        elif (player.playerX >= borderX):
            player.playerX = borderX
        
        if (player.playerY <= 0):
            player.playerY = 0
        elif (player.playerY >= borderY):
            player.playerY = borderY

        window.fill((0, 0, 0))
        background.setBackground()

        player.drawPlayer()
        cursor.displayCursor()

        pygame.display.update()
    
    pygame.quit()

if (__name__ == '__main__'):
    main()