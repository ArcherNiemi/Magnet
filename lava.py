import main
import pygame

class lava:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, cameraPos, sizing,xCenter,yCenter):
        pygame.draw.rect(main.screen, "red", pygame.Rect(round((self.x - cameraPos[0])*sizing)+xCenter, round((self.y - cameraPos[1])*sizing)+yCenter, round(self.width*sizing), round(self.height*sizing)))