import pygame

class Cursor:

    def __init__(self, window, cursorPath) -> None:
        self.window = window
        self.cursorPath = cursorPath

        self.cursorImg = pygame.image.load(cursorPath)
        self.rect = self.cursorImg.get_rect()

        pygame.mouse.set_visible(False)
    
    def displayCursor(self):
        self.rect.center = pygame.mouse.get_pos()
        self.window.blit(self.cursorImg, self.rect)