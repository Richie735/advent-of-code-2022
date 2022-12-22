from heapq import heappop, heappush
from string import ascii_lowercase

# Getting the input parameters
with open("./Day-12/input12.in") as file:
    input = file.read().strip().split()

# print(input)

numLines = len(input)
numCols = len(input[0])
map = [list(line) for line in input]

# initialize the map and positions
starts = []
for line in range(numLines):
    for col in range(numCols):
        char = map[line][col]
        if char == 'S':
            startPosition = line, col 
            starts.append((line, col))
        elif char == 'E': 
            endPosition = line, col 
        elif char == 'a':
            starts.append((line, col))    


# translate the character in height value
def translate(i, j):
    char = map[i][j]
    if char == 'S':
        return 0
    elif char == 'E':
        return 25
    elif char in ascii_lowercase:
        return ascii_lowercase.index(char)


########################
#        Part 1        #
########################
def validNeighbors(line, col):
    height = translate(line, col)
    neighbors = []

    # iterate up, right, down and left neighbors
    for i, j in [[1,0], [0,1], [-1,0], [0, -1]]:
        # save the actual neighbor cords
        ii = line + i
        jj = col + j

        if ii >= 0 and ii < len(map) and jj >= 0 and jj < len(map[0]):
            if translate(ii, jj) <= height + 1:
                neighbors.append((ii, jj))
        
    return neighbors

def Dijkstra(startPos, endPos):
    # Dijkstra Algorithm for shortest path finding
    heap = [] # cost, line, col
    heappush(heap, (0, startPos))
    isVisited = set()

    while True:
        if not heap:
            break

        cost, node = heappop(heap)
        if node not in isVisited:
            isVisited.add(node)

            if node == endPos:
                return cost
            
            for ii, jj in validNeighbors(node[0], node[1]):
                heappush(heap, (cost+1, (ii, jj)))


########################
#        Part 2        #
########################
costs = []
for start in starts:
    cost = Dijkstra(start, endPosition)
    if cost is not None:
        costs.append(cost)


########################
#  Getting the Answer  #
########################
print ("Answer to Day 12: \n part-1 => ", Dijkstra(startPosition, endPosition), "\n part-2 => ", min(costs))