# Getting the input parameters
with open("input05.in") as file:
    # initial is the starting stacks of crates
    # procedure is the moves made
    initial, procedure = (i.splitlines() for i in file.read().strip('\n').split('\n\n'))

# initializing the sctacks Dictionary
stacks = {int(digit):[] for digit in initial[-1].replace(" ","")}

# Fuction to print the stack information 
def printStacks():
    print("\n\n<=== Stacks ===>\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")

# saving the position of each stack in the text
# ex.: cranes in the second stack occupy the char number 5 in the line
positions = [index for index, char in enumerate(initial[-1]) if char != " "]
# print(positions)

# Set the starting stacks
def startStacks():
    for line in initial[:-1]:
        stackIndex = 1
        for position in positions:
            if line[position] != " ":
                stacks[stackIndex].insert(0, line[position])
            stackIndex += 1

#  Getting the Answer
def getAnswer():
    result = ""
    for stack in stacks:
        result += stacks[stack][-1]
    return result


########################
#        Part 1        #
########################
startStacks()   # initializing content

for move in procedure:
    # clear words
    move = move.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ") 
    # setting the line to a vector of ints
    move = [int(i) for i in move]
    
    # move[0] => number of iterations
    # move[1] => origin stack
    # move[2] => destination stack

    for i in range(move[0]):
        # moving crate
        crate = stacks[move[1]].pop()
        stacks[move[2]].append(crate)

# printing the result
print ("Answer to Day 05: \n part-1 => ", getAnswer())


########################
#        Part 2        #
########################

# Reseting the stacks
for i in stacks:
    stacks[i].clear()
startStacks()   # initializing content 

for move in procedure:
    # clear words
    move = move.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ") 
    # setting the line to a vector of ints
    move = [int(i) for i in move]

    # passing the crates in movement to a variable
    crates = stacks[move[1]][-move[0]:]

    # removing the crates in movement from the origin stack
    stacks[move[1]] = stacks[move[1]][:-move[0]]
    
    # putting the crates in movement to the destination stack
    for i in crates:
        stacks[move[2]].append(i)

# printing the result
print(" part-2 => ", getAnswer())