input = open('advent_of_code_2022\Day 1\input.txt', 'r')
lines = input.readlines()
array = []
sum = 0

for line in lines:
    if line  == '\n':
        array.append(sum)
        sum = 0
    else:
        sum += int(line)

input.close()
array.sort()
total = array[-1] + array[-2] + array[-3]
print(total)
