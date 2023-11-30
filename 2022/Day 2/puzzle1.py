input = open("advent_of_code_2022\Day 2\input.txt", "r")
lines = input.readlines()
score = 0

for line in lines:
    if line[2] == 'X': # Rock
        score += 1 
        if line[0] == 'A': #Rock
            score += 3
        elif line[0] == 'B': #Paper
            score += 0
        elif line[0] == 'C': #Scissors
            score += 6

    elif line[2] == 'Y': # Paper
        score += 2
        if line[0] == 'A': #Rock
            score += 6
        elif line[0] == 'B': #Paper
            score += 3
        elif line[0] == 'C': #Scissors
            score += 0

    elif line[2] == 'Z': # Scissors
        score += 3
        if line[0] == 'A': #Rock
            score += 0
        elif line[0] == 'B': #Paper
            score += 6
        elif line[0] == 'C': #Scissors
            score += 3

input.close()
print(score)
