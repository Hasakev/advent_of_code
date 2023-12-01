input = open('./input.txt', 'r')
lines = input.readlines()

sum = 0
for line in lines:
    array = []
    for char in line:
        if char.isdigit():
            array.append(char)
    if array:
        number = int(array[0] + array[-1])
        sum += number
            
print(sum)
