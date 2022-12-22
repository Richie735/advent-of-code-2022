from string import ascii_letters

# Getting the input parameters
with open("./Day-03/input03.in") as file:
    input = [i for i in file.read().strip().split("\n")]

#print(input)

# Priority
# a -> z = 1 -> 26
# A -> Z = 27 -> 52

totalPriority = 0

# Go through the input
for bag in input:
    # locate the middle point
    middle = len(bag)//2
    
    # seting each compartment
    first_compartment = set(bag[:middle])
    second_compartment = set(bag[middle:])
    
    # Go throug the alphabet
    for priority, char in enumerate(ascii_letters):
        # Check if the letter is in both compartments
        if char in first_compartment and char in second_compartment:
            totalPriority += priority + 1    # it start in 0, so we need to + 1

########################
#        Part 2        #
########################

totalBadges=0
endOfGroup = 3
totalPriority2 = 0

# Go through the input with steps of 3
for group in range(0, len(input), 3):
    # Putting the 3 bags in one vector
    bags = input[group:endOfGroup]
    endOfGroup += 3

    # Go throug the alphabet
    for priority, char in enumerate(ascii_letters):
        # Check if the letter is in the three bags
        if char in bags[0] and char in bags[1] and char in bags[2]:
            totalPriority2 += priority + 1    # it start in 0, so we need to + 1

########################
#  Getting the Answer  #
########################
print ("Answer to Day 03: \n part-1 => ", totalPriority, "\n part-2 => ", totalPriority2)
