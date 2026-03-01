import main
import pygame
from main import screen, SCREEN_HEIGHT, SCREEN_WIDTH

pygame.init()

LIGHT_BLUE = (100, 150, 255)
BLUE = (0,0,255)

LEVELS = [["level 1", 1], ["level tate", 2]]

LEVEL_BOX_SIZE = 110
SPACING = 20
TITLE_SPACING = 100

FONT_TITLE = pygame.font.SysFont("arial", 70)
FONT_BOX = pygame.font.SysFont("arial", 35)

def draw():
    screen.fill(LIGHT_BLUE)

    titleText = FONT_TITLE.render("Magent Fun", 1, "black")
    screen.blit(titleText, (SCREEN_WIDTH / 2 - titleText.get_width()/2, TITLE_SPACING/2 - titleText.get_height()/2))

    drawBoxes = True
    x = SPACING
    y = TITLE_SPACING
    count = 0
    while(drawBoxes):
        pygame.draw.rect(screen, BLUE, pygame.Rect(x, y, LEVEL_BOX_SIZE,LEVEL_BOX_SIZE))

        boxText = FONT_BOX.render(str(LEVELS[count][1]), 1, "white")
        screen.blit(boxText, (x + LEVEL_BOX_SIZE / 2 - boxText.get_width() / 2, y + LEVEL_BOX_SIZE / 2 - boxText.get_height() / 2))

        x += LEVEL_BOX_SIZE + SPACING
        if (x + LEVEL_BOX_SIZE > SCREEN_WIDTH):
            x = SPACING
            y += LEVEL_BOX_SIZE + SPACING

        count += 1
        if(count >= len(LEVELS)):
            drawBoxes = False
        
    pygame.display.flip()

def run():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickBoxes = True
                x = SPACING
                y = TITLE_SPACING
                count = 0
                while(clickBoxes):
                    pygame.draw.rect(screen, BLUE, pygame.Rect(x, y, LEVEL_BOX_SIZE,LEVEL_BOX_SIZE))
                    if(x <= event.pos[0] and x + LEVEL_BOX_SIZE >= event.pos[0] and y <= event.pos[1] and y + LEVEL_BOX_SIZE >= event.pos[1]):
                        main.main(LEVELS[count][0])
                        break

                    x += LEVEL_BOX_SIZE + SPACING
                    if (x + LEVEL_BOX_SIZE > SCREEN_WIDTH):
                        x = SPACING
                        y += LEVEL_BOX_SIZE + SPACING

                    count += 1
                    if(count >= len(LEVELS)):
                        clickBoxes = False
        
        draw()

if __name__ == "__main__":
    run()