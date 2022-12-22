# Getting the input parameters
with open("./Day-06/input06.in") as file:
    input = file.read()

#print(input) 


########################
#        Part 1        #
########################
for i in range(4, len(input)):
    # Divide the different characters
    marker = set(input[(i-4):i])
    if len(marker) == 4:    # if size = 4, all characters are different
        print("Answer to Day 06: \n part-1 => ", i)
        break


########################
#        Part 2        #
########################
# Equal as part 1 but is 14 instead of 4
for i in range(14, len(input)):
    # Divide the different characters
    marker = set(input[(i-14):i])
    if len(marker) == 14:    # if size = 14, all characters are different
        print(" part-2 => ", i)
        break
