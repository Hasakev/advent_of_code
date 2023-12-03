input = open('./input.txt', 'r')
lines = input.readlines()
sum = 0
temp_num = ""
for j in range(len(lines)): 
    symbol = set()
    dict = {}
    i = 0
    line = lines[j]
    line = line.strip('\n')
    while i < len(line):
        if line[i] == '*':
            symbol.add(i)
            dict[i] = []    
        i += 1
    if len(symbol) > 0:
        for k in (j-1, j, j + 1):
            focus = lines[k]
            m = 0
            while m < len(focus):
                if focus[m].isdigit():
                    digits = []
                    while focus[m].isdigit():
                        digits.append(m)
                        temp_num += focus[m]
                        m += 1
                    for digit in digits:
                        a = False
                        for symb in symbol:
                            if (digit - 1) == symb or (digit + 1) == symb or digit == symb:
                                dict[symb].append(temp_num)
                                a = True
                                break
                        if a:
                            break
                    temp_num = ""
                m += 1 
        for key in dict:
            if len(dict[key]) == 2:
                sum += int(dict[key][0]) * int(dict[key][1])
print(sum)