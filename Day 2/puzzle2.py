input = open("advent_of_code_2022\Day 2\input.txt", "r")
lines = input.readlines()
score = 0
rock = 1
paper = 2
scissors = 3

for line in lines:
    if line[0] == 'A': # Rock 
        if line[2] == 'X': #Lose
            score += 0 
            score += scissors  #pick 
        elif line[2] == 'Y': #Draw
            score += 3
            score += rock
        elif line[2] == 'Z': #Win
            score += 6
            score += paper

    elif line[0] == 'B': # Paper
        if line[2] == 'X': #Lose
            score += 0 
            score += rock #pick 
        elif line[2] == 'Y': #Draw
            score += 3
            score += paper
        elif line[2] == 'Z': #Win
            score += 6
            score += scissors

    elif line[0] == 'C': # Scissors 
        if line[2] == 'X': #Lose
            score += 0 
            score += paper #pick 
        elif line[2] == 'Y': #Draw
            score += 3
            score += scissors
        elif line[2] == 'Z': #Win
            score += 6
            score += rock

input.close()
print(score)
