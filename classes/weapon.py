import os
import sys
sys.path.append('../')

import random

import pygame
from pygame import mixer

from config import VOLUME
from constants import WEAPON_ID_LIST
from classes.bullet import Bullet

class Weapon:

    def __init__(self, window, weaponID) -> None:
        self.window = window

        # The input weaponID show always be valid
        self.weaponID = weaponID

        self.audioDir = f"./audio/{weaponID}"
        self.audioFiles = os.listdir(self.audioDir)
    
    def fire(self, playerX, playerY, destX, destY):
        # Spawns a bullet everytime when the player fires
        bullet = Bullet(self.window, self.weaponID, playerX, playerY, destX, destY)
        self.playSound()

        return bullet
    
    def playSound(self):
        audioFile = random.choice(self.audioFiles)
        audioFile = f"{self.audioDir}/{audioFile}"

        mixer.music.load(audioFile)
        mixer.music.set_volume(VOLUME / 100)
        mixer.music.play(loops=0)
