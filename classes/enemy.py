import pygame

from config import ENEMY_IMAGES_PATH

class Enemy:

    def __init__(self, window, imgPath, x, y, colRadius) -> None:
        self.window = window
        
        self.imgPath = f'{ENEMY_IMAGES_PATH}/{imgPath}'
        self.img = pygame.image.load(self.imgPath)

        self.imgWidth = self.img.get_width()
        self.imgHeight = self.img.get_height()

        self.alive = True

        # This is actually the top-left coords
        self.x = x
        self.y = y

        self.centerX = self.x + self.imgWidth / 2
        self.centerY = self.y + self.imgHeight / 2

        self.rightBottomX = self.x + self.imgWidth
        self.rightBottomY = self.y + self.imgHeight

        self.colRadius = colRadius
    
    def draw(self):
        self.window.blit(self.img, (self.x, self.y))

        # Draws a cicle on the enemy with collision radius
        # pygame.draw.circle(self.window, (0, 255, 0), (self.centerX, self.centerY), self.colRadius, 0)

        # Draws dots on the top-left & right-bottom corner
        # pygame.draw.circle(self.window, (255, 0, 0), (self.x, self.y), 3, 0)
        # pygame.draw.circle(self.window, (0, 0, 255), (self.rightBottomX, self.rightBottomY), 3, 0)