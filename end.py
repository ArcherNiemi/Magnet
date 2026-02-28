import main
import pygame

class end:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        pygame.draw.rect(main.screen, "green", pygame.Rect(self.x, self.y, self.width, self.height))