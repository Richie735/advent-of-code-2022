# Getting the input parameters
with open("./Day-08/input08.in") as file:
    # store the input as a matrix
    input = [line.strip() for line in file.readlines()]

# print(input)

numlines = len(input)
numCols = len(input[0])

# left line + right line + top col(- edges) + bottom col(- edges)
borders = (numlines*2) + ((numCols-2)*2)
# all borders are visible
visible = borders

highestScore = 0

for line in range(1, numlines-1):     # From 1 to -1 because borders already added
    for col in range(1, numCols-1):
       
        # Getting the side trees
        up = [input[line-i][col] for i in range(1, line+1)]
        right = [input[line][col+i] for i in range(1, numCols-col)]
        down = [input[line+i][col] for i in range(1, numlines-line)]
        left = [input[line][col-i] for i in range(1, col+1)]
        
        ########################
        #        Part 1        #
        ########################
        if max(up)<input[line][col] or max(right)<input[line][col] or max(down)<input[line][col] or max(left)<input[line][col]:
            # if is the highest in any direction is visible
            visible += 1


        ########################
        #        Part 2        #
        ########################
        # reseting the score of the actual tree
        ScenicScore = 1

        # iterate through all sides
        for trees in (up, right, down, left):
            sideScore = 0
            for i in range(len(trees)):
                # if tree is smaller score++
                if trees[i] < input[line][col]:
                    sideScore += 1
                # if is bigger or equal score++ but block view
                elif trees[i] >= input[line][col]:
                    sideScore += 1
                    break
            
            # Incrising Scenic Score
            ScenicScore *= sideScore
    
        # Checking if the new high Score
        if ScenicScore > highestScore:
            highestScore = ScenicScore

            
########################
#  Getting the Answer  #
########################
print ("Answer to Day 08: \n part-1 => ", visible, "\n part-2 => ", highestScore)
