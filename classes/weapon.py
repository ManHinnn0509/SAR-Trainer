import os
import sys
sys.path.append('../')

import random

import pygame
from pygame import mixer

from config import VOLUME
from constants import WEAPON_ID_LIST, BULLET_MOVE_SPEED

class Weapon:

    def __init__(self, window, weaponID) -> None:
        self.window = window

        # The input weaponID show always be valid
        self.weaponID = weaponID
        self.bulletSpeed = BULLET_MOVE_SPEED[weaponID]

        self.audioDir = f"./audio/{weaponID}"
        self.audioFiles = os.listdir(self.audioDir)
        print(self.audioFiles)
    
    def playSound(self):
        audioFile = random.choice(self.audioFiles)
        audioFile = f"{self.audioDir}/{audioFile}"

        mixer.music.load(audioFile)
        mixer.music.set_volume(VOLUME / 100)
        mixer.music.play(loops=0)
