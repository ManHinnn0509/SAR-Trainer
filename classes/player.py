import pygame

class Player:

    def __init__(self, window, imgPath, x, y) -> None:
        self.window = window
        
        self.imgPath = imgPath
        self.playerImg = pygame.image.load(imgPath)

        self.playerImgWidth = self.playerImg.get_width()
        self.playerImgHeight = self.playerImg.get_height()

        # Current top-left coords of the player
        self.playerX = x
        self.playerY = y

        # The coords. of the middle (center?) of the player
        self.centerX = self.playerX + self.playerImgWidth / 2
        self.centerY = self.playerY + self.playerImgHeight / 2
    
    def updateCoords(self, dx, dy):
        self.playerX += dx
        self.playerY += dy

        self.centerX = self.playerX + self.playerImgWidth / 2
        self.centerY = self.playerY + self.playerImgHeight / 2

    def resizePlayerImg(self, scaleX, scaleY):
        self.playerImg = pygame.transform.scale(self.playerImg, (scaleX, scaleY))
        
        self.playerImgWidth = self.playerImg.get_width()
        self.playerImgHeight = self.playerImg.get_height()

    def drawPlayer(self):
        self.window.blit(self.playerImg, (self.playerX, self.playerY))