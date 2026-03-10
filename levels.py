from block import block
from end import end
from wall import wall
from spring import spring
from lava import lava

def getLevel(level):
    blocks = []
    walls = []
    springs = []
    lavaList = []

    if(level == "level 1"):
        blocks.append(block(100, 100, 20, 20, "white", 0.2, 10))

        walls.append(wall(100,200,300,5,"y"))
        walls.append(wall(500, 200, 300, 5, "y"))
        walls.append(wall(500, 400, 200, 5, "y"))
        walls.append(wall(500, 200, 5, 200, "x"))
        walls.append(wall(300, 300, 5, 300, "x"))

        springs.append(spring(480, 300, 20, 40, 30, "l"))
        springs.append(spring(500, 580, 40, 20, 30, "u"))
        springs.append(spring(305, 400, 20, 40, 30, "r"))

        endArea = end(750,250,50,100)

        levelBox = [800,600]

    elif(level == "level 2"):
        blocks.append(block(75, 75, 20, 20, "white", 0.2, 10))

        walls.append(wall(0, 150, 600, 5, "y"))
        walls.append(wall(450, 150, 5, 300, "x"))
        walls.append(wall(600, 300, 5, 300, "x"))
        walls.append(wall(150, 445, 300, 5, "y"))

        springs.append(spring(780, 150, 20, 40, 30, "l"))
        springs.append(spring(0, 400, 20, 40, 30, "r"))

        endArea = end(375,275,50,50)

        levelBox = [800,600]
    
    elif(level == "level 3"):
        blocks.append(block(75, 75, 20, 20, "white", 0.2, 10))

        walls.append(wall(300,75,5,300,"x"))
        walls.append(wall(0,450,300,5,"y"))
        walls.append(wall(150,600,400,5,"y"))
        walls.append(wall(550,375,5,300,"x"))
        walls.append(wall(500,375,100,5,"y"))
        walls.append(wall(600,0,5,250,"x"))
        walls.append(wall(550,250,100,5,"y"))
        walls.append(wall(800,250,300, 5,"y"))
        walls.append(wall(800,250,5,350,"x"))
        walls.append(wall(900,600,200,5,"y"))
        walls.append(wall(950,75,5,175,"x"))

        springs.append(spring(580,105,20,40,30,"l"))
        springs.append(spring(530,470,20,40,30,"l"))
        springs.append(spring(230,605,40,20,30,"d"))
        springs.append(spring(330,780,40,20,30,"u"))
        springs.append(spring(430,605,40,20,30,"d"))
        springs.append(spring(830,780,40,20,30,"u"))

        endArea = end(1125,350,75,150)
        levelBox = [1200, 800]

    elif(level == "level 4"):
        blocks.append(block(75, 75, 20, 20, "white", 0.2, 10))

        lavaList.append(lava(200, 200, 400, 400))

        endArea = end(750,250,50,100)
        levelBox = [800,600]

    elif(level == "level 5"):
        blocks.append(block(75, 75, 20, 20, "white", 0.2, 10))

        for i in range(6):
            lavaList.append(lava(i*1200+200, 200, 400, 400))
            lavaList.append(lava(i*1200+800, 0, 400, 400))

        endArea = end(7999,0,1,800)
        levelBox = [8000,600]
    
    return [blocks, walls, springs, lavaList, endArea, levelBox]