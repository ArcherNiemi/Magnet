from block import block
from end import end
from wall import wall
from spring import spring

def getLevel(level):
    blocks = []
    walls = []
    springs = []
    
    if(level == "level 1"):
        blocks.append(block(100, 100, 20, 20, "white", 0.1, 3))

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
    
    return [blocks, walls, springs, endArea]