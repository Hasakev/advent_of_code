def puzzle_solver(marker):
    file = open("Day 6\input.txt", "r")
    array = []
    line = file.read()
    for i in range(len(line)):
        array.append(line[i])
        if len(array) >= marker:
            if check(array, marker):
                file.close()
                return len(array)

                        
def check(array, marker):
    new_array = array[-marker:]
    if len(set(new_array)) == len(new_array):
        return True
    return False
                       

print(puzzle_solver(4)) # puzzle 1 
print(puzzle_solver(14)) # puzzle 2