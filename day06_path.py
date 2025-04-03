
# Takes data from input as a list
def extractInput():
    with open("/Users/joshtagle/Downloads/advent-2024/input.txt") as file:
        data = list(file)
    for index in range(len(data) - 1):
        data[index] = data[index][:-1]
    return data

# Formats map as 2-dimensional list
def formatMap(data):
    return [list(line) for line in data]

# Moves guard forward or turns guard at obstacle
def move(map, x, y, direction):
    ahead = map[y + direction[1]][x + direction[0]]
    footprintCharacters = ["", "r", "d", "u", "l"]
    footprint = footprintCharacters[direction[0] + 2 * direction[1]]
    if footprint in ahead:
        return 0, 0, 0, True
    else:
        map[y][x] += footprint
    guardCharacters = ["", ">", "V", "^", "<"]
    # Implies guard at obstacle
    if ahead == "#":
        direction = [-direction[1], direction[0]]
        map[y][x] += guardCharacters[direction[0] + 2 * direction[1]]
        return x, y, direction, False
    # Impiles guard may move forward
    else:
        x += direction[0]
        y += direction[1]
        map[y][x] += guardCharacters[direction[0] + 2 * direction[1]]
        return x, y, direction, False


# Checks if guard faces position within map
def checkAheadInBounds(map, x, y, direction):
    x += direction[0]
    y += direction[1]
    if x >= 0 and x < len(map[0]) and y >= 0 and y < len(map):
        return True
    return False

# Finds guard coordinates and initial direction
def findStart(map):
    for y in range(len(map)):
        for x in range(len(map[0])):
            directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
            guardCharacters = ["^", ">", "V", "<"]
            if not map[y][x] in [".", "#"]:
                guardCharacter = map[y][x]
                return x, y, directions[guardCharacters.index(guardCharacter)]

# Counts unique coordinates in completed guard path
def countX(map):
    count = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "X":
                count += 1
    return count + 1

# Counts unique obstacles that result in loops within completed guard path
def countLoop(map):
    count = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            mapEdit = [row[:] for row in map]
            # Places obstacle in empty space
            if mapEdit[y][x] == ".":
                print("Running trial at (" + str(x) + ", " + str(y) + ")...")
                mapEdit[y][x] = "#"
                count += patrol(mapEdit)
    return count

# Runs guard path
def patrol(map):
    x, y, direction = findStart(map)
    while checkAheadInBounds(map, x, y, direction):
        x, y, direction, loop = move(map, x, y, direction)
        if loop:
            return 1
    return 0
        

def run():
    map = formatMap(extractInput())
    print(countLoop(map))