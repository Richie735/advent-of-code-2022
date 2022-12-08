# Getting the input parameters
with open("input01.in") as file:
    input = [i for i in file.read().strip().split("\n")]

#print(input)


# Initialize variables
max_cal = 0     # Elf with the most calories
max_cal2 = 0    # Elf with the second most calories
max_cal3 = 0    # Elf with the third most calories
count_cal = 0


# Go through the input
for item in input:
    
    # Checking how much each Elf carries
    if item == '':      # Changin the Elf
        count_cal = 0
    else:               # Adding the calories to the current Elf
        num = int(item)
        count_cal += num

    # Updating the top 3
    if count_cal > max_cal:
        max_cal3 = max_cal2
        max_cal2 = max_cal
        max_cal = count_cal
    elif count_cal > max_cal2:
        max_cal3 = max_cal2
        max_cal2 = count_cal
    elif count_cal > max_cal3:
        max_cal3 = count_cal


########################
#  Getting the Answer  #
########################
print ("Answer to Day 01: \n part-1 => ", max_cal, "\n part-2 => ", (max_cal+ max_cal2 + max_cal3))