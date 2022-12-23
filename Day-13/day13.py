from functools import cmp_to_key

# Getting the input parameters
with open("./Day-13/input13.in") as file:
    input = file.read().strip().split("\n\n")
    inputt = file.read().strip().replace("\n\n", "\n").split("\n")

# print(input)

def compare(left, right):
    # check if one is list and the other is int
    # convert the int to a list if true
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
    
    # now both objects have the same type
    # int make the comparison
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left == right:
            return 0
        return -1   
    # list use recursive comparison
    elif isinstance(left, list) and isinstance(right, list):
        i = 0
        while i < len(left) and i < len(right):
            aux = compare(left[i], right[i])
            if aux == 1:
                return 1
            elif aux == -1:
                return -1
            
            i += 1
        
        if i == len(left):
            if len(left) == len(right):
                return 0

            # left end first
            return 1

        # right end first
        return -1


########################
#        Part 1        #
########################
answer = 0

for i, line in enumerate(input):
    left, right = map(eval, line.split("\n"))

    if compare(left, right) == 1:
        answer += i + 1


########################
#        Part 2        #
########################

# https://stackoverflow.com/questions/32752739/how-does-the-functools-cmp-to-key-function-work

list = list(map(eval, inputt))
list.append([[2]])
list.append([[6]])
list = sorted(list, key=cmp_to_key(compare), reverse=True)

for i, aux in enumerate(list):
    if aux == [[2]]:
        l = i + 1
    if aux == [[6]]:
        r = i + 1


########################
#  Getting the Answer  #
########################
print ("Answer to Day 13: \n part-1 => ", answer, "\n part-2 => ", (l * r))