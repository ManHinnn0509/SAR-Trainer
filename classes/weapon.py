import os
import sys
import time
sys.path.append('../')

import random

import pygame
from pygame import mixer

from config import VOLUME, INFINITE_BULLETS
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
        self.reloadAudioFile = f"{self.reloadAudioDir}/{self.reloadAudioFile}"
        self.reloadAudioLen = mixer.Sound(self.reloadAudioFile).get_length()

        self.clipSize = WEAPON_CLIP_SIZE[weaponID]
        self.clip = self.clipSize

        self.reloading = False

        self.reloadStartTime = None
        self.reloadEndTime = None
    
    def fire(self, playerX, playerY, destX, destY):

        # This has to go first
        self.clipCheck()
        
        if (self.clip == 0):
            return

        if (self.reloading):
            return

        # Spawns a bullet everytime when the player fires
        bullet = Bullet(self.window, self.weaponID, playerX, playerY, destX, destY)

        audioFile = random.choice(self.audioFiles)
        audioFile = f"{self.audioDir}/{audioFile}"
        self.playSound(audioFile)

        if not (INFINITE_BULLETS):
            self.clip = self.clip - 1

        return bullet

    def playSound(self, audioFilePath):
        mixer.music.load(audioFilePath)
        mixer.music.set_volume(VOLUME / 100)
        mixer.music.play(loops=0)

    def reload(self):
        # Return if the clip is full
        if (self.clip == self.clipSize):
            return
        
        if (self.reloadEndTime == None):
            self.reloadEndTime = time.time() + self.reloadAudioLen
        
        if not (self.reloading):
            self.reloadEndTime = time.time() + self.reloadAudioLen
        
        # Return if it's already reloading
        else:
            return

        if (time.time() < self.reloadEndTime):
            self.playSound(self.reloadAudioFile)
            self.reloading = True

    def clipCheck(self):
        if (self.reloadEndTime != None):
            if (time.time() >= self.reloadEndTime):
                # Set self.reloadEndTime back to None to prevent bug
                # This will make the ammo goes infinite
                self.reloadEndTime = None
                self.clip = self.clipSize
                self.reloading = False