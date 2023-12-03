input = open('./input.txt', 'r')
lines = input.readlines()
sum = 0

temp_num = ""
for j in range(len(lines)):
    symbol = set() 
    i = 0
    line = lines[j]
    line = line.strip('\n')
    while i < len(line):
        if not (line[i].isdigit() or line[i] == '.' or line[i] == '\n'):
            symbol.add(i)
            symbol.add(i + 1)
            symbol.add(i - 1)
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
                        if digit in symbol:
                            sum += int(temp_num)
                            break
                    temp_num = ""
                m += 1 
                
print(sum)