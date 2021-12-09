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
        self.bulletSpeed = BULLET_MOVE_SPEED[weaponID] * 0.3

        # Status of the bullet
        # Turn this to False if:
        # - The bullet hits something
        # - Out of range
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

        # OMG! Working solution!
        # https://coderedirect.com/questions/55065/shooting-a-bullet-in-pygame-in-the-direction-of-mouse
        
        self.dir = (destX - srcX, destY - srcY)
        self.length = math.hypot(*self.dir)

        if (self.length == 0.0):
            self.dir = (0, -1)
        else:
            self.dir = (self.dir[0] / self.length, self.dir[1] / self.length)

        self.angle = math.degrees(math.atan2(-1 * self.dir[1], self.dir[0]))

        self.dispX = self.dir[0] * self.bulletSpeed
        self.dispY = self.dir[1] * self.bulletSpeed

        self.bullet = self.__createBullet()

    def __createBullet(self):
        # These 2 values will be changed in the future
        # Since the bullet size / color of each weapons are different
        # This is for the default weapon (Magnum)
        bulletSize = (55, 2)
        bulletColor = (255, 255, 255)

        bullet = pygame.Surface(bulletSize).convert_alpha()
        bullet.fill(bulletColor)
        bullet = pygame.transform.rotate(bullet, self.angle)

        return bullet

    def draw(self, enemyList):

        # The parameter 'enemyList' is for checking if the bullet hits an enemy
        # If it does, then set 'alive' to False

        # Test | Draw a circle on the mouse's coords
        # pygame.draw.circle(self.window, (0, 255, 0), (self.currX, self.currY), 10, 0)
        
        bulletRect = self.bullet.get_rect(center=(self.currX, self.currY))
        self.window.blit(self.bullet, bulletRect)

        self.currX += self.dispX
        self.currY += self.dispY

        # Checks if the bullet reached the border
        if ((self.currX >= WIDTH) or (self.currX <= 0)):
            self.alive = False
        
        if ((self.currY >= HEIGHT) or (self.currY <= 0)):
            self.alive = False
        
        # Checks if the bullet hitted an enemy
        if (self.hittedEnemy(enemyList)):
            self.alive = False
    
    def hittedEnemy(self, enemyList):
        # Check for each enemies on screen
        for enemy in enemyList.enemies:

            dx = math.pow((enemy.centerX - self.currX), 2)
            dy = math.pow((enemy.centerY - self.currY), 2)
            dist = math.sqrt(dx + dy)

            colDist = enemy.colRadius * 2        # r * 2
            if (dist < colDist):
                # Remove the current loop's enemy by setting it's 'alive' to False
                enemy.alive = False
                return True
        
        return False


'''
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

        self.angle = -1 * math.degrees(math.atan2(-1 * (destY - srcY), destX - srcX))
        # print(f'self.angle = {self.angle}')

        self.dispX = self.bulletSpeed * math.cos(self.angle)
        self.dispY = self.bulletSpeed * math.sin(self.angle)
        print(f'dispX = {self.dispX} | dispY = {self.dispY}')

    
    def draw(self):
        # Test | Draw a circle on the mouse's coords
        pygame.draw.circle(self.window, (0, 255, 0), (self.currX, self.currY), 10, 0)

        # NOT DONE YET
        # WRONG CALCULATION IN HERE
        self.currX += self.dispX
        self.currY += self.dispY

        # Checks if the bullets reached the border
        if ((self.currX >= WIDTH) or (self.currX <= 0)):
            self.alive = False
        
        if ((self.currY >= HEIGHT) or (self.currY <= 0)):
            self.alive = False

        # Draws a red dot on player's position & mouse position
        # pygame.draw.circle(self.window, (255, 0, 0), (self.srcX, self.srcY), 10, 0)
        # pygame.draw.circle(self.window, (0, 0, 255), (self.destX, self.destY), 10, 0)

        # midPoint = (int((self.destX + self.srcX) / 2), int ((self.destY + self.srcY) / 2))
        # pygame.draw.circle(self.window, (255, 0, 255), midPoint, 10, 0)

        pygame.draw.line(self.window, (255, 0, 255), (self.srcX, self.srcY), (self.destX, self.destY))
'''