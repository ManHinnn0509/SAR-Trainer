import os
import sys
sys.path.append('../')

import random

import pygame
from pygame import mixer

from config import VOLUME
from constants import WEAPON_CLIP_SIZE
from classes.bullet import Bullet

class Weapon:

    def __init__(self, window, weaponID) -> None:
        self.window = window

        # The input weaponID show always be valid
        self.weaponID = weaponID

        self.audioDir = f"./audio/{weaponID}/fire"
        self.audioFiles = os.listdir(self.audioDir)

        self.reloadAudioDir = f"./audio/{weaponID}/reload"
        self.reloadAudioFiles = os.listdir(self.reloadAudioDir)

        self.clipSize = WEAPON_CLIP_SIZE[weaponID]
        self.clip = self.clipSize
    
    def fire(self, playerX, playerY, destX, destY):
        # Spawns a bullet everytime when the player fires
        bullet = Bullet(self.window, self.weaponID, playerX, playerY, destX, destY)

        audioFile = random.choice(self.audioFiles)
        audioFile = f"{self.audioDir}/{audioFile}"
        self.playSound(audioFile)

        return bullet
    
    def playSound(self, audioFilePath):
        mixer.music.load(audioFilePath)
        mixer.music.set_volume(VOLUME / 100)
        mixer.music.play(loops=0)
