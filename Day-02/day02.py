# Getting the input parameters
with open("input02.in") as file:
    guide = [i for i in file.read().strip().split("\n")]

# print(guide)

# A | X - Rock - 1
# B | Y - Paper - 2
# C | Z - Scissors - 3
# 0-Loss | 3-Draw | 6-Win
# score = shape + outcome

# Dictionary
scores = {
                # Game  Outcome     Score
    "A X":4,    # A X    Draw    (1 + 3) = 4
    "A Y":8,    # A Y    Win     (2 + 6) = 8
    "A Z":3,    # A Z    Loss    (3 + 0) = 3
    "B X":1,    # B X    Loss    (1 + 0) = 1
    "B Y":5,    # B Y    Draw    (2 + 3) = 5
    "B Z":9,    # B Z    Win     (3 + 6) = 9
    "C X":7,    # C X    Win     (1 + 6) = 7
    "C Y":2,    # C Y    Loss    (2 + 0) = 2
    "C Z":6     # C Z    Draw    (3 + 3) = 6
}

# DESIRED OUTCOMES
# Changed the values of the outcomes depending on the rules
# X = LOSS, Y = DRAW, Z = WIN
# (got values looking at table above)
desired_outcomes = {
    "A X":3, "A Y":4, "A Z":8, 
    "B X":1, "B Y":5, "B Z":9, 
    "C X":2, "C Y":6, "C Z":7 
}

final_score = 0
for round in guide:
    final_score += scores[round]

total_score_p2 = 0
for round in guide:
    total_score_p2 += desired_outcomes[round]

# Getting the Answer
print ("Answer to Day 02: \n part-1 => ", final_score,
     "\n part-2 => ", total_score_p2)