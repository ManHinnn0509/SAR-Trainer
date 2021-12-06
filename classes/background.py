import pygame

class Background:

    def __init__(self, window, bgPath) -> None:
        self.window = window
        self.bgPath = bgPath

        self.bgImg = pygame.image.load(bgPath)
        self.bgWidth = self.bgImg.get_width()
        self.bgHeight = self.bgImg.get_height()
    
    def resize(self, scaleX, scaleY):
        self.bgImg = pygame.transform.scale(self.bgImg, (scaleX, scaleY))
        self.bgWidth = self.bgImg.get_width()
        self.bgHeight = self.bgImg.get_height()
    
    def setBackground(self):
        self.window.blit(self.bgImg, (0, 0))