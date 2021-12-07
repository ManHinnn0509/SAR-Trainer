import pygame

from constants import BULLET_MOVE_SPEED

class Bullet:
    def __init__(self, window, weaponID) -> None:
        self.window = window
        self.weaponID = weaponID
        self.alive = False

        self.bulletSpeed = BULLET_MOVE_SPEED[weaponID]
    
    def draw(self, srcX, srcY, destX, destY):
        self.alive = True
        print(srcX, srcY)
        print(destX, destY)
        pass