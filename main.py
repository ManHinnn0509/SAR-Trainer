import pygame

from classes import Player, Background
from config import WIDTH, HEIGHT
from constants import *

def main():

    # Init program
    pygame.init()

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('SAR Trainer')

    # Set background
    background = Background(window, './img/bg/LoginSceneBG.png')
    background.resize(WIDTH, HEIGHT)
    background.setBackground()

    # Init player
    player = Player(window, './img/plastic.png', int(WIDTH / 2), int(HEIGHT / 2))
    player.resizePlayerImg(
        int(player.playerImg.get_width() * 0.1),
        int(player.playerImg.get_height() * 0.1)
    )

    borderX = WIDTH - player.playerImgWidth
    borderY = HEIGHT - player.playerImgHeight

    run = True
    while (run):
        
        dt = clock.tick(60)
        run = checkQuit()

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
        pygame.display.update()
    
    pygame.quit()

def checkQuit():
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            return False
    
    return True

if (__name__ == '__main__'):
    main()