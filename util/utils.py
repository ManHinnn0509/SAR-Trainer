import random

def randDouble():
    return random.random()

def randInt(start, end):
    return int(random.randrange(start, end))

def randChoice(l: list):
    return random.choice(l)

def calcStats(firedBullets, killedEnemies):
    """
        Returning tuple: (killedEnemies, firedBullets, missed, hitRate)
    """
    missed = firedBullets - killedEnemies

    hitRate = 0 if (firedBullets == 0) else ((killedEnemies / firedBullets) * 100)
    hitRate = f"{hitRate:.2f} %"

    return (killedEnemies, firedBullets, missed, hitRate)
