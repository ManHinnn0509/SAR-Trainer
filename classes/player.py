import pygame

class Player:

    def __init__(self, window, imgPath, x, y) -> None:
        self.window = window
        
        self.imgPath = imgPath
        self.playerImg = pygame.image.load(imgPath)

        self.playerImgWidth = self.playerImg.get_width()
        self.playerImgHeight = self.playerImg.get_height()

        self.playerX = x
        self.playerY = y
    
    def resizePlayerImg(self, scaleX, scaleY):
        self.playerImg = pygame.transform.scale(self.playerImg, (scaleX, scaleY))
        
        self.playerImgWidth = self.playerImg.get_width()
        self.playerImgHeight = self.playerImg.get_height()

    def drawPlayer(self):
        self.window.blit(self.playerImg, (self.playerX, self.playerY))