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
    #find game id
    id = int(data[0].split("Game ")[1])
    bag = data[1].split(';') 
    for trial in bag:
        entry = trial.split(',')
        for cubes in entry:
            for type in dict:
                if type in cubes:
                    dict[type] -= int(cubes.split(type)[0])
        if dict['green'] < 0 or dict['red'] < 0 or dict['blue'] < 0:
            banned.add(id)
        # reset dict
        dict = {
            'green': 13,
            'red': 12,
            'blue': 14,
        }
    if id not in banned:
        sum += id

print(sum)