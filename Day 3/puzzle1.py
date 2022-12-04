input = open("advent_of_code_2022\Day 3\input.txt", "r")
lines = input.readlines()
sum = 0

for line in lines:
    array = []
    br = int(len(line)/2)
    c1 = line[0:br]
    c2 = line[br:]

    for i in range(len(c1)):
        for j in range(len(c2)):
            if c1[i] == c2[j] and c1[i] not in array:
                array.append(c1[i])

    number = ord(array[0])

    # print(array[0], number, sep=", ")
    # Using ASCII nature, ord:
    if number >= 65 and number <= 90: # Upper case values, A to Z worth 27 to 52
        number -= 38 # tp get A (and following) = 27
    if number >= 97 and number <= 122: # Lower case values, a to z worth 1 to 26
    
        number -= 96 # to get a (and following) = 1
    
    sum += number


print(sum)
