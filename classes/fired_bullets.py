from classes.bullet import Bullet

class FiredBullets:

    def __init__(self) -> None:
        self.bullets = []
    
    def addBullet(self, bullet: Bullet):
        self.bullets.append(bullet)
    
    def updateBullets(self, enemyList):

        for bullet in self.bullets:
            
            if (bullet.alive):
                bullet.draw(enemyList)
            
            else:
                self.bullets.remove(bullet)