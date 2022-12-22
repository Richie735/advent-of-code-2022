# Getting the input parameters
with open("./Day-10/input10.in") as file:
    # store the input as a matrix
    input = file.read().strip().split("\n")

# print(input)

########################
#        Part 1        #
########################
x = 1
cycle = 0
checks = [20, 60, 100, 140, 180, 220]
answer = 0

for line in input:
    command = line.split(" ")

    cycle += 1
    
    if cycle in checks:
        answer += cycle * x
        
    if command[0] == "addx":
        cycle += 1

        if cycle in checks:
            answer += cycle * x

        v = int(command[1])
        x += v
        
########################
#        Part 2        #
########################
actualX = 1
cycle = 0
value = [1] * 241

for line in input:
    command = line.split(" ")

    if command[0] == "noop":
        cycle += 1
        value[cycle] = actualX

    elif command[0] == "addx":
        v = int(command[1])

        value[cycle + 1] = actualX
        actualX += v

        cycle += 2
        value[cycle] = actualX


answer2 = [[None] * 40 for i in range(6)]
for row in range(6):
    for col in range(40):
        if abs(value[row * 40 + col] - (col)) <= 1:
            answer2[row][col] ="#"
        else:
            answer2[row][col] =" "


########################
#  Getting the Answer  #
########################
print ("Answer to Day 10: \n part-1 => ", answer, "\n part-2 => ")
for row in answer2:
    print("".join(row))