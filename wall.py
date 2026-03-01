import main
import pygame

class wall:
    def __init__(self,x,y,width,height, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
    
    def draw(self, cameraPos):
        pygame.draw.rect(main.screen, "black", pygame.Rect(self.x - cameraPos[0], self.y - cameraPos[1], self.width, self.height))