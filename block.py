import main
import pygame

class block:
    def __init__(self, x, y, width, height, color, speed, friction):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed / 100
        self.friction = friction / 100
        self.momentumX = 0
        self.momentumY = 0
    
    def draw(self):
        pygame.draw.rect(main.screen, self.color, pygame.Rect(round(self.x), round(self.y), self.width, self.height))

    def move(self):
        self.x += self.momentumX
        self.y += self.momentumY
        if (self.momentumX > 0):
            self.momentumX -= self.friction
            if(self.momentumX < 0):
                self.momentumX = 0
        elif(self.momentumX < 0):
            self.momentumX += self.friction
            if(self.momentumX > 0):
                self.momentumX = 0
        if (self.momentumY > 0):
            self.momentumY -= self.friction
            if(self.momentumY < 0):
                self.momentumY = 0
        elif(self.momentumY < 0):
            self.momentumY += self.friction
            if(self.momentumY > 0):
                self.momentumY = 0

    def movementUpdate(self, mouseX, mouseY):
        distanceX = self.x - mouseX
        distanceY = self.y - mouseY

        self.momentumX -= self.speed * distanceX
        self.momentumY -= self.speed * distanceY

    def checkBounds(self):
        if(self.x < 0 or self.x + self.width > main.SCREEN_WIDTH):
            self.momentumX = -self.momentumX
        if(self.y < 0 or self.y + self.height > main.SCREEN_HEIGHT):
            self.momentumY = -self.momentumY
        
        for i in range(len(main.walls)):
            if(self.y + self.height > main.walls[i].y and self.y < main.walls[i].y + main.walls[i].height and self.x + self.width > main.walls[i].x and self.x < main.walls[i].x + main.walls[i].width):
                if(main.walls[i].type == "y"):
                    self.momentumY = -self.momentumY
                elif(main.walls[i].type == "x"):
                    self.momentumX = -self.momentumX
        
        for i in range(len(main.springs)):
            if(self.y + self.height > main.springs[i].y and self.y < main.springs[i].y + main.springs[i].height and self.x + self.width > main.springs[i].x and self.x < main.springs[i].x + main.springs[i].width):
                if(main.springs[i].type == "l"):
                    self.momentumX = -main.springs[i].power
                elif(main.springs[i].type == "r"):
                    self.momentumX = main.springs[i].power
                elif(main.springs[i].type == "u"):
                    self.momentumY = -main.springs[i].power
                elif(main.springs[i].type == "d"):
                    self.momentumY = main.springs[i].power