# Getting the input parameters
with open("./Day-11/input11.in") as file:
    input = file.read().strip().split("\n\n")

# print(input)


class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation
        self.test = test
        self.inspections = 0

    def __str__(self):
        return f"{self.items} - {self.operation} - {self.test} - {self.inspections}"


# initialize monkeys data
monkeys = []
monkeys2 = []
for i, input in enumerate(input):
    data = input.split("\n")
    items = list(map(int, data[1][2:].split(" ", 2)[2].split(", ")))
    operation = data[2][2:].split(" ", 3)[3].split(" ")

    divBy = int(data[3][2:].split(" ")[-1])
    true = int(data[4][4:].split(" ")[-1])
    false = int(data[5][4:].split(" ")[-1])

    # Atribute values to each monkey
    monkeys.append(Monkey(items, operation, [divBy, true, false]))
    monkeys2.append(Monkey(items, operation, [divBy, true, false]))


def manageOperation(operation, value):
    # I will assume that 
    #   the first value is always "old"
    #   the possible operation is + or *
    if operation[2] == "old":
        value2 = value
    else:
        value2 = operation[2]

    if operation[1] == "*":
        return int(value) * int(value2)
    else:
        return int(value) + int(value2)
        

def getAnswer(monk):
    # Getting the 2 mos inspectors
    answer = [m.inspections for m in monk]
    answer = sorted(answer)
    return answer[-1] * answer[-2]


########################
#        Part 1        #
########################
for round in range(20):
    for i in range(len(monkeys)):
        monkey = monkeys[i]
        for item in monkey.items:
            item = manageOperation(monkey.operation, item) // 3

            if item % monkey.test[0] == 0:
                monkeys[monkey.test[1]].items.append(item)
            else:
                monkeys[monkey.test[2]].items.append(item)
            
            monkeys[i].inspections += 1

            monkey.items = []
        

########################
#        Part 2        #
########################

# Thx Reddit
big_mod = 1
for monkey in monkeys2:
    big_mod *= monkey.test[0]

for round in range(10000):
    for i in range(len(monkeys2)):
        monkey = monkeys2[i]
        for item in monkey.items:
            item = (manageOperation(monkey.operation, item)) % big_mod

            if item % monkey.test[0] == 0:
                monkeys2[monkey.test[1]].items.append(item)
            else:
                monkeys2[monkey.test[2]].items.append(item)
            

            monkeys2[i].inspections += 1

        monkey.items = []


########################
#  Getting the Answer  #
########################
print ("Answer to Day 11: \n part-1 => ", getAnswer(monkeys), "\n part-2 => ", getAnswer(monkeys2))