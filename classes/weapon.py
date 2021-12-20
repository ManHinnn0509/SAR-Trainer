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
        print(f"[Debug] {len(self.reloadAudioFiles)} found")

        # Only 1 reload audio, so just get the first one
        self.reloadAudioFile = self.reloadAudioFiles[0]
        self.reloadAudioLen = mixer.Sound(f"{self.reloadAudioDir}/{self.reloadAudioFile}").get_length()

        self.clipSize = WEAPON_CLIP_SIZE[weaponID]
        self.clip = self.clipSize

        self.clipEmpty = False
        self.reloading = False

        self.reloadStartTime = None
    
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
