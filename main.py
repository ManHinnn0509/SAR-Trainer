import os
import pygame
from pygame import mixer

from util.utils import calcStats, randInt, randChoice
from classes import *
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

    # Init background
    background = Background(window, BACKGROUND_IMAGE_PATH)
    background.resize(WIDTH, HEIGHT)

    # Init cursor
    cursor = Cursor(window, CURSOR_IMAGE_PATH)

    # Init player
    player = Player(window, PLAYER_IMAGE_PATH, int(WIDTH / 2), int(HEIGHT / 2))
    player.resizePlayerImg(
        int(player.playerImg.get_width() * 0.1),
        int(player.playerImg.get_height() * 0.1)
    )

    # Init weapon, and also a list thats records bullet states
    weapon = Weapon(window, 'GunMagnum')
    firedBullets = FiredBullets()

    # Init data & variable for enemies
    enemyImages = [i for i in os.listdir(ENEMY_IMAGES_PATH) if (i.endswith('.png'))]
    enemies = EnemyList(MAX_ENEMY_AMOUNT)

    # Init stats display on top-left corner
    textDisplay = TextDisplay(window, "Comic Sans MS", 15)

    # --- Varibles, maybe also constants

    run = True

    borderX = WIDTH - player.playerImgWidth
    borderY = HEIGHT - player.playerImgHeight

    while (run):
        dt = clock.tick(60)
        
        window.fill((0, 0, 0))
        background.setBackground()

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

                    bullet = weapon.fire(
                        player.centerX, player.centerY,
                        mouseX, mouseY
                    )
                    
                    if (bullet != None):
                        firedBullets.addBullet(bullet)

                    # print(f'Player: {player.playerX}, {player.playerY}')
                    # print(f'Mouse: {mouseX}, {mouseY}')

                # RIGHT
                elif (event.button == 3):
                    # print('RIGHT Mouse DOWN')
                    pass
        
        enemies.updateEnemies()
        firedBullets.updateBullets(enemies)

        # Spawn enemy(ies) until it reaches the maximum amount
        while not (enemies.isFull()):
            e = createEnemy(window, enemyImages)
            enemies.addEnemy(e)

        # Put these 2 lines after the update methods
        # So that the player & cursor won't be covered by the enemy(ies)
        player.drawPlayer()
        cursor.displayCursor()

        stats = calcStats(firedBullets.firedBulletsAmount, enemies.killedEnemiesAmount)
        info = f"""
        Enemy(ies) killed: {stats[0]}
        Fired bullets: {stats[1]}
        Hit rate: {stats[3]}
        """
        textDisplay.displayMultipleLine(info, (255, 255, 255), 0, 0)

        # Get key pressed by user / player
        keys = pygame.key.get_pressed()

        # Player movement
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
        
        # Reload
        if (keys[pygame.K_r]):
            pass

        # ESC
        if (keys[pygame.K_ESCAPE]):
            # ESC key to exit
            run = False
        
        player.updateCoords(dx, dy, borderX, borderY)

        pygame.display.update()
    
    pygame.quit()

    stats = calcStats(firedBullets.firedBulletsAmount, enemies.killedEnemiesAmount)
    print(f"Enemy(ies) killed: {stats[0]}")
    print(f"Fired bullets: {stats[1]}")
    print(f"Missed shots: {stats[2]}")
    print(f"Hit rate: {stats[3]}")

    print('--- End of Program ---')

def createEnemy(window, enemyImages) -> Enemy:

    # A constant value to avoid the enemy spawning beyond screen
    BORDER_X = 100
    BORDER_Y = 100

    e = Enemy(
        window,
        randChoice(enemyImages),
        randInt(0 + BORDER_X, WIDTH - BORDER_X),
        randInt(0 + BORDER_Y, HEIGHT - BORDER_Y),
        ENEMY_COLLISION_RADIUS
    )

    return e

if (__name__ == '__main__'):
    main()