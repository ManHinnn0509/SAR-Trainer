import pygame
import math

from config import WIDTH, HEIGHT
from constants import BULLET_MOVE_SPEED

class Bullet:
    def __init__(self, window, weaponID, srcX, srcY, destX, destY) -> None:
        self.window = window

        # Weapon ID, assume all the input weaponIDs are valid
        self.weaponID = weaponID
        
        # Bullet speed, get from the constant dict
        self.bulletSpeed = BULLET_MOVE_SPEED[weaponID] / 100

        # Status of the bullet
        # Turn this to False if:
        # - The bullet hits something
        # - Out of sight
        # - Maximum distance reached (?)
        self.alive = True

        # Current position / coords of the bullet
        self.currX = srcX
        self.currY = srcY

        # Source position / coords
        self.srcX = srcX
        self.srcY = srcY

        # Dest position / coords
        self.destX = destX
        self.destY = destY

        self.angle = -1 * math.degrees(math.atan2(destY - srcY, destX - srcX))
        # print(f'self.angle = {self.angle}')

        self.dispX = self.bulletSpeed * math.cos(self.angle)
        self.dispY = self.bulletSpeed * math.sin(self.angle)
        # print(f'dx = {self.dispX} | dy = {self.dispY}')

    
    def draw(self):
        # Test | Draw a circle on the mouse's coords
        pygame.draw.circle(self.window, (0, 255, 0), (self.currX, self.currY), 10, 0)

        # NOT DONE YET
        # WRONG CALCULATION IN HERE
        self.currX += self.dispX
        self.currY += self.dispY

        # Checks if the bullets reached the border
        if (self.currX >= WIDTH):
            self.alive = False
        
        if (self.currY >= HEIGHT):
            self.alive = False

        # Draws a red dot on player's position & mouse position
        # pygame.draw.circle(self.window, (255, 0, 0), (self.srcX, self.srcY), 10, 0)
        # pygame.draw.circle(self.window, (0, 0, 255), (self.destX, self.destY), 10, 0)