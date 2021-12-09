from classes.bullet import Bullet

class FiredBullets:

    def __init__(self) -> None:
        self.bullets = []
        self.firedBulletsAmount = 0
    
    def addBullet(self, bullet: Bullet):
        self.bullets.append(bullet)
        self.firedBulletsAmount += 1
    
    def updateBullets(self, enemyList):

        for bullet in self.bullets:
            
            if (bullet.alive):
                bullet.draw(enemyList)
            
            else:
                self.bullets.remove(bullet)