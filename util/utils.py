import random

def randDouble():
    return random.random()

def randInt(start, end):
    return int(random.randrange(start, end))

def randChoice(l: list):
    return random.choice(l)