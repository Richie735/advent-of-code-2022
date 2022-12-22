# Getting the input parameters
with open("./Day-09/input09.in") as file:
    input = file.read().strip().split("\n")

# print(input)

# Class with the cords
class Cords:
    def __init__(self):
        self.x=0
        self.y=0

# Verify is Head and Tail are together
def isTouching(hX, hY, tX, tY):
    return abs(hX - tX) <= 1 and abs(hY - tY) <= 1

# Map with the actions of each Direction
moveMap = {
    "U": [0, 1],    # Up
    "R": [1, 0],    # Right
    "D": [0, -1],   # Down
    "L": [-1, 0]    # Left 
}


########################
#        Part 1        #
########################

# Execute the movent
def movementHt(head, tail, moveX, moveY):
    head.x += moveX
    head.y += moveY

    if not isTouching(head.x, head.y, tail.x, tail.y):
        objectiveX = 0 if head.x == tail.x else (head.x - tail.x) / abs(head.x - tail.x)
        objectiveY = 0 if head.y == tail.y else (head.y - tail.y) / abs(head.y - tail.y)

        tail.x += objectiveX
        tail.y += objectiveY

visited = set()

Head = Cords()
Tail = Cords()

for move in input:
    direction, steps = move.split(" ")
    moveX, moveY = moveMap[direction]

    for step in range(int(steps)):
        movementHt(Head, Tail, moveX, moveY)
        visited.add((Tail.x, Tail.y))

        
########################
#        Part 2        #
########################

rope = [[0, 0] for _ in range(10)]

# Execute the movent
def movementRope( moveX, moveY):
    rope[0][0] += moveX
    rope[0][1] += moveY

    for i in range(1, 10):
        headX, headY = rope[i - 1]
        tailX, tailY = rope[i]

        if not isTouching(headX, headY, tailX, tailY):
            objectiveX = 0 if headX == tailX else (headX - tailX) / abs(headX - tailX)
            objectiveY = 0 if headY == tailY else (headY - tailY) / abs(headY - tailY)

            tailX += objectiveX
            tailY += objectiveY
        
        rope[i] = [tailX, tailY]

ropeVisited = set()
ropeVisited.add(tuple(rope[-1]))

for move in input:
    direction, steps = move.split(" ")
    moveX, moveY = moveMap[direction]

    for i in range(int(steps)):
        movementRope(moveX, moveY)
        ropeVisited.add(tuple(rope[-1]))


########################
#  Getting the Answer  #
########################
print ("Answer to Day 09: \n part-1 => ", len(visited), "\n part-2 => ",len(ropeVisited))