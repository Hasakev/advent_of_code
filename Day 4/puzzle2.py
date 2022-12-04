input = open("advent_of_code_2022\Day 4\input.txt", "r")
lines = input.readlines()
overlap = 0

for line in lines:
    list = line.strip().split(',')
    e1 = list[0].split('-')
    e1max = int(e1[1])
    e1min = int(e1[0])

    e2 = list[1].split('-')
    e2max = int(e2[1])
    e2min = int(e2[0])

    e1list = []
    e2list = []

    for i in range(e1max):
        if e1min > e1max:
            break
        e1list.append(e1min)
        e1min += 1

    for k in range(e2max):
        if e2min > e2max:
            break
        e2list.append(e2min)
        e2min += 1
    
    # basically the same as puzzle one but any instead of all (haha)
    check = any(item in e1list for item in e2list)
    check2 = any(item in e2list for item in e1list)

    if check is True or check2 is True:
        overlap += 1

print(overlap)
