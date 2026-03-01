import pygame
import sys 
import time
from levels import getLevel

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
levelBox = []
currentLevel = ""

cameraPos = [100, 100]

def draw(endArea):
    screen.fill(BLUE)

    endArea.draw(cameraPos)

    for i in range(len(walls)):
        walls[i].draw(cameraPos)

    for i in range(len(springs)):
        springs[i].draw(cameraPos)

    for i in range(len(blocks)):
        blocks[i].draw(cameraPos)

    pygame.display.flip()

def main(level):
    global currentLevel
    currentLevel = level
    setUpLevel()

    currentTime = 0
    timerGoing = False

    print("there")
    running = True
    while running:
        deltaTime = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r:
                    resetGame()
    
        mouseButtons = pygame.mouse.get_pressed()
        if mouseButtons[0]:
            timerGoing = True
            mousePos = pygame.mouse.get_pos()
            for i in range(len(blocks)):
                blocks[i].movementUpdate(mousePos[0] + cameraPos[0], mousePos[1] + cameraPos[1])

        for i in range(len(blocks)):
            blocks[i].speedCap()
            blocks[i].move()
            blocks[i].checkBounds(levelBox)
            cameraPos[0] = blocks[i].x - SCREEN_WIDTH/2
            cameraPos[1] = blocks[i].y - SCREEN_HEIGHT/2
            if(endArea.x < blocks[i].x + blocks[i].width and endArea.x + endArea.width > blocks[i].x and endArea.y < blocks[i].y + blocks[i].height and endArea.y + endArea.height > blocks[i].y):
                endGameScreen(round(currentTime,2))
                running = False
        adjustCamera()
        if(timerGoing):
            currentTime += 1/FPS
        draw(endArea)

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
    print("nowhere")
    main(currentLevel)

def setUpLevel():
    global blocks
    global walls
    global springs
    global endArea
    global levelBox
    selectedLevel = getLevel(currentLevel)
    blocks = selectedLevel[0]
    walls = selectedLevel[1]
    springs = selectedLevel[2]
    endArea = selectedLevel[3]
    levelBox = selectedLevel[4]

def adjustCamera():
    if(cameraPos[0] < 0):
        cameraPos[0] = 0
    elif(cameraPos[0] > levelBox[0] - SCREEN_WIDTH):
        cameraPos[0] = levelBox[0] - SCREEN_WIDTH
    if(cameraPos[1] < 0):
        cameraPos[1] = 0
    elif(cameraPos[1] > levelBox[1] - SCREEN_HEIGHT):
        cameraPos[1] = levelBox[1] - SCREEN_HEIGHT

if __name__ == "__main__":
    main("level 1")