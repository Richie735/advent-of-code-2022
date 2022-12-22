# Getting the input parameters
with open("./Day-07/input07.in") as file:
    input = [i for i in file.read().strip().split("\n")]

#print(input)


# $     -       Command
#       ls      List -> do nothing

#       cd      Change dir
#           /   Go to root
#           ..  Step back
#           any Change path

########################
#      "Compiler"      #
########################
# Dictionary with all directories path and his sizes
directories = {"/root":0}

path="/root"
for line in input:
    # check if is a command
    if line[0] == '$':
        # if ls, do nothing
        if line[2:4] == "ls":
            pass
        # if dir, change path
        elif line[2:4] == "cd":
            # back to root
            if line[5] == '/':
                path="/root"

            # step back
            elif line[5:7] == "..":
                path = path[0:path.rfind("/")]

            # change path
            else:
                # get name -> add to path -> add path to dictionary
                dir = line[5:]
                path = path + '/' + dir
                directories.update({path:0})

    # check if is listing directories
    elif line[0:3] == "dir":
        # do nothing
        pass

    # if neither, is a file
    else:  
        # Get the 
        size = int(line[:line.find(" ")])

        actualDir = path
        for i in range(path.count("/")):
            directories[actualDir] += size
            actualDir = actualDir[:actualDir.rfind("/")]


########################
#        Part 1        #
########################
sum = 0

for directory in directories:
    if directories[directory] < 100000:
        sum += directories[directory]


########################
#        Part 2        #
########################
requiredSpace = 30000000 - (70000000 - directories["/root"])
chosenOnes = []

for directory in directories:
    if requiredSpace <= directories[directory]:
        chosenOnes.append(directories[directory])


########################
#  Getting the Answer  #
########################
print ("Answer to Day 07: \n part-1 => ", sum, "\n part-2 => ", min(chosenOnes))
