import main
import pygame

SPEED_CAP = 20
SPEED_LIMIT = 15
SPEED_LIMIT_REDUCTION = 3
DISTANCE_CAP = 200

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

        if(distanceX > DISTANCE_CAP):
            distanceX = DISTANCE_CAP
        elif(distanceX < -DISTANCE_CAP):
            distanceX = -DISTANCE_CAP
        if(distanceY > DISTANCE_CAP):
            distanceY = DISTANCE_CAP
        elif(distanceY < -DISTANCE_CAP):
            distanceY = -DISTANCE_CAP

        self.momentumX -= self.speed * distanceX
        self.momentumY -= self.speed * distanceY

    def speedCap(self):
        if(self.momentumX > SPEED_LIMIT):
            self.momentumX -= SPEED_LIMIT_REDUCTION
        elif(self.momentumX < -SPEED_LIMIT):
            self.momentumX += SPEED_LIMIT_REDUCTION
        if(self.momentumY > SPEED_LIMIT):
            self.momentumY -= SPEED_LIMIT_REDUCTION
        elif(self.momentumY < -SPEED_LIMIT):
            self.momentumY += SPEED_LIMIT_REDUCTION

        if(self.momentumX > SPEED_CAP):
            self.momentumX = SPEED_CAP
        elif(self.momentumX < -SPEED_CAP):
            self.momentumX = -SPEED_CAP
        if(self.momentumY > SPEED_CAP):
            self.momentumY = SPEED_CAP
        elif(self.momentumY < -SPEED_CAP):
            self.momentumY = -SPEED_CAP


    def checkBounds(self):
        if(self.x < 0 or self.x + self.width > main.SCREEN_WIDTH):
            self.momentumX = -self.momentumX
        if(self.y < 0 or self.y + self.height > main.SCREEN_HEIGHT):
            self.momentumY = -self.momentumY
        
        for i in range(len(main.walls)):
            if(self.y + self.height > main.walls[i].y and self.y < main.walls[i].y + main.walls[i].height and self.x + self.width > main.walls[i].x and self.x < main.walls[i].x + main.walls[i].width):
                if(main.walls[i].type == "y"):
                    if(self.momentumY > 0):
                        self.momentumY = -self.momentumY - 1.2
                    elif(self.momentumY < 0):
                        self.momentumY = -self.momentumY + 1.2
                elif(main.walls[i].type == "x"):
                    if(self.momentumX > 0):
                        self.momentumX = -self.momentumX - 1.2
                    elif(self.momentumX < 0):
                        self.momentumX = -self.momentumX + 1.2
        
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