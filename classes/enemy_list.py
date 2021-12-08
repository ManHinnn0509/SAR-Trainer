import pygame

from classes.enemy import Enemy

class EnemyList:

    def __init__(self, maxAmount) -> None:
        self.enemies = []
        self.maxAmount = maxAmount
    
    def addEnemy(self, enemy):
        if (len(self.enemies) != self.maxAmount):
            self.enemies.append(enemy)
    
    def updateEnemies(self):
        for enemy in self.enemies:

            if (enemy.alive):
                enemy.draw()
            
            else:
                self.enemies.remove(enemy)
    
    def isFull(self):
        return (len(self.enemies) == self.maxAmount)