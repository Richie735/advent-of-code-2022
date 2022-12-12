# Getting the input parameters
with open("input04.in") as file:
    input = [i for i in file.read().strip().split("\n")]

# print(input)

fully_contained = 0;
overlap = 0;

# Loop through the input
for line in input:
    # Split each line and transform in int
    elf1, elf2 = line.split(",")
    elf1 = [int(i) for i in elf1.split("-")]
    elf2 = [int(i) for i in elf2.split("-")]

    ########################
    #        Part 1        #
    ########################
    # Checking if fully contained
    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        fully_contained += 1
    elif elf2[0] <= elf1[0] and elf2[1] >= elf1[1]:
        fully_contained += 1


    ########################
    #        Part 2        #
    ########################
    # Checking for existing overlap sections
    if elf1[0] in range(elf2[0], elf2[1]+1) or elf1[1] in range(elf2[0], elf2[1]+1):
        overlap += 1
    elif elf2[0] in range(elf1[0], elf1[1]+1) or elf2[1] in range(elf1[0], elf1[1]+1):
        overlap += 1


########################
#  Getting the Answer  #
########################
print ("Answer to Day 04: \n part-1 => ", fully_contained, "\n part-2 => ", overlap)
