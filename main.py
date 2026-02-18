import pygame
import sys 
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

clock = pygame.time.Clock()
FPS = 60

pygame.display.set_caption("Magnet Fun")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
LIGHT_BLUE = (110, 188, 224)

ENDGAME_FONT = pygame.font.SysFont("Arial", 36)


blocks = []
walls = []
springs = []

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
        pygame.draw.rect(screen, self.color, pygame.Rect(round(self.x), round(self.y), self.width, self.height))
    
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
        if(self.x < 0 or self.x + self.width > SCREEN_WIDTH):
            self.momentumX = -self.momentumX
        if(self.y < 0 or self.y + self.height > SCREEN_HEIGHT):
            self.momentumY = -self.momentumY
        
        for i in range(len(walls)):
            if(self.y + self.height > walls[i].y and self.y < walls[i].y + walls[i].height and self.x + self.width > walls[i].x and self.x < walls[i].x + walls[i].width):
                if(walls[i].type == "y"):
                    self.momentumY = -self.momentumY
                elif(walls[i].type == "x"):
                    self.momentumX = -self.momentumX
        
        for i in range(len(springs)):
            if(self.y + self.height > springs[i].y and self.y < springs[i].y + springs[i].height and self.x + self.width > springs[i].x and self.x < springs[i].x + springs[i].width):
                if(springs[i].type == "l"):
                    self.momentumX = -springs[i].power
                elif(springs[i].type == "r"):
                    self.momentumX = springs[i].power
                elif(springs[i].type == "u"):
                    self.momentumY = -springs[i].power
                elif(springs[i].type == "d"):
                    self.momentumY = springs[i].power

class end:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        pygame.draw.rect(screen, "green", pygame.Rect(self.x, self.y, self.width, self.height))

class wall:
    def __init__(self,x,y,width,height, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
    
    def draw(self):
        pygame.draw.rect(screen, "black", pygame.Rect(self.x, self.y, self.width, self.height))

class spring:
    def __init__(self,x,y,width,height,power, type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.power = power
        self.type = type
    
    def draw(self):
        pygame.draw.rect(screen, "orange", pygame.Rect(self.x, self.y, self.width, self.height))

def draw(endArea):
    screen.fill(BLUE)

    endArea.draw()

    for i in range(len(walls)):
        walls[i].draw()

    for i in range(len(springs)):
        springs[i].draw()

    for i in range(len(blocks)):
        blocks[i].draw()

    pygame.display.flip()

def main():
    currentTime = 0
    level = "level tate"
    # blocks.append(block(100, 100, 40, 40, "red", 0.02, 0.2))
    if(level == "level 1"):
        blocks.append(block(100, 100, 20, 20, "green", 0.1, 3))

        walls.append(wall(500, 200, 300, 5, "y"))
        walls.append(wall(500, 400, 200, 5, "y"))
        walls.append(wall(500, 200, 5, 200, "x"))
        walls.append(wall(300, 300, 5, 300, "x"))

        springs.append(spring(480, 300, 20, 40, 15, "l"))
        springs.append(spring(500, 580, 40, 20, 15, "u"))
        springs.append(spring(305, 400, 20, 40, 15, "r"))

        endArea = end(750,250,50,100)
    elif(level == "level tate"):
        blocks.append(block(75, 75, 20, 20, "white", 0.1, 3))

        walls.append(wall(0, 150, 600, 5, "y"))
        walls.append(wall(450, 150, 5, 300, "x"))
        walls.append(wall(600, 300, 5, 300, "x"))
        walls.append(wall(150, 445, 300, 5, "y"))

        springs.append(spring(780, 150, 20, 40, 20, "l"))
        springs.append(spring(0, 400, 20, 40, 20, "r"))

        endArea = end(375,275,50,50)


    timerGoing = False

    running = True
    while running:
        deltaTime = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    running = False
                    resetGame()
    
        mouseButtons = pygame.mouse.get_pressed()
        if mouseButtons[0]:
            timerGoing = True
            mousePos = pygame.mouse.get_pos()
            for i in range(len(blocks)):
                blocks[i].movementUpdate(mousePos[0], mousePos[1])

        for i in range(len(blocks)):
            blocks[i].move()
            blocks[i].checkBounds()
            if(endArea.x < blocks[i].x + blocks[i].width and endArea.x + endArea.width > blocks[i].x and endArea.y < blocks[i].y + blocks[i].height and endArea.y + endArea.height > blocks[i].y):
                endGameScreen(round(currentTime,2))
                running = False
        if(timerGoing):
            currentTime += 1/FPS
        draw(endArea)
    
    pygame.quit()
    sys.exit()

def endGameScreen(endTime):
    pygame.draw.rect(screen, LIGHT_BLUE, pygame.Rect(250, 100, 300, 400))
    endText = ENDGAME_FONT.render("you won", 1, "black")
    screen.blit(endText, (SCREEN_WIDTH / 2 - endText.get_width() / 2, 150))
    endTimeText = ENDGAME_FONT.render(f"time: {endTime}", 1, "black")
    screen.blit(endTimeText, (SCREEN_WIDTH / 2 - endTimeText.get_width() / 2, 250))
    pygame.display.flip()
    time.sleep(1)
    resetGame()

def resetGame():
    global blocks
    global walls
    global springs
    blocks = []
    walls = []
    springs = []
    main()

if __name__ == "__main__":
    main()