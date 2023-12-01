input = open('./input.txt', 'r')
lines = input.readlines()
dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
sum = 0
for line in lines:
    array = []
    string = ""
    for char in line:
        for word in dict:
            if word in string:
                array.append(dict[word])
                string = "" + string[-1]
        if char.isdigit():
            array.append(char)
        elif char.isalpha():
                string += char
    if array:
        number = int(array[0] + array[-1])
        sum += number
            
print(sum)
