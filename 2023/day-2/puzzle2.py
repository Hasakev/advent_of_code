input = open('./input.txt', 'r')
lines = input.readlines()
sum = 0
banned = set()
dict = {
    'green': 13,
    'red': 12,
    'blue': 14,
}
for line in lines:
    data = line.split(':')
    # Find game id
    game_id = int(data[0].split("Game ")[1])
    bag = data[1].split(';')
    red_max = 0
    green_max = 0
    blue_max = 0
    for trial in bag:
        entry = trial.split(',')
        for cubes in entry:
            info = cubes.split(' ')
            type = info[2].strip('\n')
            amount = int(info[1])
            dict[type] -= amount
            if type == 'red':
                red_max = max(red_max, amount)
            elif type == 'green':
                green_max = max(green_max, amount)
            elif type == 'blue':
                blue_max = max(blue_max, amount)
        # Reset dict
        dict = {
            'green': 13,
            'red': 12,
            'blue': 14,
        }
    sum += red_max * green_max * blue_max
    

print(sum)
