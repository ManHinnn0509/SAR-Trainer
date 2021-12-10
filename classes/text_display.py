import pygame

class TextDisplay:

    def __init__(self, window, fontName, fontSize) -> None:
        self.window = window

        self.fontName = fontName
        self.fontSize = fontSize

        self.font = pygame.font.SysFont(fontName, fontSize)
    
    def display(self, text: str, color: tuple, x: int, y: int, antialias=False):
        textSurface = self.font.render(text, antialias, color)
        self.window.blit(textSurface, (x, y))
    
    def displayMultipleLine(self, text: str, color: tuple, x: int, y: int, antialias=False):
        lines = text.split("\n")

        for line in lines:
            textSurface = self.font.render(line, antialias, color)

            self.window.blit(textSurface, (x, y))
            y += self.fontSize