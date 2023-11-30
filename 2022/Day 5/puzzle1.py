input = open("advent_of_code_2022\Day 5\input.txt", "r")
lines = input.readlines()
message = ''

one = []
two = []
three = []
four = []
five = []
six = []
seven = []
eight = []
nine = []

array = [one,two,three,four,five,six,seven,eight,nine]

for line in lines:
    test = line.strip()
    if test == '':
        continue
    if test[0] == '[':
        one.append(line[1])
        two.append(line[5])
        three.append(line[9])
        four.append(line[13])
        five.append(line[17])
        six.append(line[17 + 4])
        seven.append(line[17 + 4 + 4])
        eight.append(line[17 + 4 + 4 + 4])
        nine.append(line[17 + 4 + 4 + 4 + 4])
    
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i][j] == " ":
                    array[i].pop(j)

    elif test[0] == 'm':
        instruction = line.strip().replace("move", "").replace("from", ":").replace("to", ":").split(":")
        amount = int(instruction[0])
        source = int(instruction[1]) - 1
        dest = int(instruction[2]) - 1
        for i in range(amount):
            array[dest].insert(0, array[source][0])
            array[source].pop(0)

for i in range(len(array)):
    print(array[i][0])


            
