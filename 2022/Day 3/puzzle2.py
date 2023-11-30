input = open("advent_of_code_2022\Day 3\input.txt", "r")
lines = input.readlines()
sum = 0
array = []
count = 0

for line in lines:
    if len(array) < 3:
        array.append(line.strip())
    else:
        count += 1
        arr = []
        for i in range(len(array[0])):
            for j in range(len(array[1])):
                for k in range(len(array[2])):
                    if array[0][i] == array[1][j] and array[0][i] == array[2][k] and array[1][j] == array[2][k] and array[0][i] not in arr:
                        arr.append(array[0][i])
                        
        print(arr)
        number = ord(arr[0])

        # print(array[0], number, sep=", ")
        # Using ASCII nature, ord:
        if number >= 65 and number <= 90: # Upper case values, A to Z worth 27 to 52
            number -= 38 # tp get A (and following) = 27
        if number >= 97 and number <= 122: # Lower case values, a to z worth 1 to 26         
            number -= 96 # to get a (and following) = 1

        print(number)
        sum += number
        array = []
        array.append(line.strip())

ar = [lines[297].strip(), lines[298].strip(), lines[299].strip()]
for i in range(len(ar[0])):
            for j in range(len(ar[1])):
                for k in range(len(ar[2])):
                    if ar[0][i] == ar[1][j] and ar[0][i] == ar[2][k] and ar[1][j] == ar[2][k]:
                        potato = (ar[0][i])
p = ord(potato) - 38
print(p)

print(sum + p)