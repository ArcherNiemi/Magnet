import main
import pygame

class spring:
    def __init__(self,x,y,width,height,power, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.power = power
        self.type = type
    
    def draw(self, cameraPos):
        pygame.draw.rect(main.screen, "orange", pygame.Rect(self.x - cameraPos[0], self.y - cameraPos[1], self.width, self.height))