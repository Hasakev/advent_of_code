input = open('advent_of_code_2022\Day 1\input.txt', 'r')
lines = input.readlines()
top = 0
sum = 0

for line in lines:
    if line  == '\n':
        if sum > top:
            top = sum
            sum = 0
        else:
            sum = 0
    else:
        sum += int(line)

input.close()
print(top)
