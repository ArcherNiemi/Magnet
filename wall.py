import main
import pygame

class wall:
    def __init__(self,x,y,width,height, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
    
    def draw(self, cameraPos, sizing,xCenter,yCenter):
        pygame.draw.rect(main.screen, "black", pygame.Rect(round((self.x - cameraPos[0])*sizing)+xCenter, round((self.y - cameraPos[1])*sizing)+yCenter, round(self.width*sizing), round(self.height*sizing)))