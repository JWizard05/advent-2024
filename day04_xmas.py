
# Takes data from input as a list
def extractInput():
    with open("/Users/joshtagle/Downloads/advent-2024/input.txt") as file:
        data = list(file)
    for index in range(len(data) - 1):
        data[index] = data[index][:-1]
    return data

# Formats search as 2-dimensional list
def formatSearch(data):
    return [list(line) for line in data]

# Counts XMAS occurrences at given coordinates
def countXmasHere(search, x, y):
    totalXmas = 0
    # Implies XMAS west
    if x >= 3 and "".join(search[y][x - 3:x + 1])[::-1] == "XMAS":
        totalXmas += 1
    # Implies XMAS east
    if x <= len(search[0]) - 4 and "".join(search[y][x:x + 4]) == "XMAS":
        totalXmas += 1
    # Implies XMAS north
    if y >= 3:
        searchSlice = []
        for displacement in range(4):
            searchSlice.append(search[y - displacement][x])
        if "".join(searchSlice) == "XMAS":
            totalXmas += 1
    # Implies XMAS south
    if y <= len(search) - 4:
        searchSlice = []
        for displacement in range(4):
            searchSlice.append(search[y + displacement][x])
        if "".join(searchSlice) == "XMAS":
            totalXmas += 1
    # Implies XMAS northwest
    if x >= 3 and y >= 3:
        searchSlice = []
        for displacement in range(4):
            searchSlice.append(search[y - displacement][x - displacement])
        if "".join(searchSlice) == "XMAS":
            totalXmas += 1
    # Implies XMAS northeast
    if x <= len(search[0]) - 4 and y >= 3:
        searchSlice = []
        for displacement in range(4):
            searchSlice.append(search[y - displacement][x + displacement])
        if "".join(searchSlice) == "XMAS":
            totalXmas += 1
    # Implies XMAS southwest
    if x >= 3 and y <= len(search) - 4:
        searchSlice = []
        for displacement in range(4):
            searchSlice.append(search[y + displacement][x - displacement])
        if "".join(searchSlice) == "XMAS":
            totalXmas += 1
    # Implies XMAS southeast
    if x <= len(search[0]) - 4 and y <= len(search) - 4:
        searchSlice = []
        for displacement in range(4):
            searchSlice.append(search[y + displacement][x + displacement])
        if "".join(searchSlice) == "XMAS":
            totalXmas += 1
    return totalXmas

# Counts XMAS occurrences through all coordinates
def countXmas(search):
    totalXmas = 0
    for y in range(len(search)):
        for x in range(len(search[0])):
            if search[y][x] == "X":
                xmasCount = countXmasHere(search, x, y)
                if xmasCount > 0:
                    print(str(xmasCount) + " XMAS found at (" + str(x) + ", " + str(y) + ")!")
                    totalXmas += xmasCount
    return totalXmas

# Counts CrossMAS occurrences at given coordinates
def checkCrossmasHere(search, x, y):
    # Retrieves characters at northwest, northeast, southeast, and southwest corners
    crossSlice = [search[y - 1][x - 1], search[y - 1][x + 1], search[y + 1][x + 1], search[y + 1][x - 1]]
    validCrossSlices = ["MMSS", "SMMS", "SSMM", "MSSM"]
    if "".join(crossSlice) in validCrossSlices:
        return True
    return False

# Counts CrossMAS occurrences through all coordinates
def countCrossmas(search):
    totalCrossmas = 0
    for y in range(len(search) - 1):
        for x in range(len(search[0]) - 1):
            if x > 0 and y > 0 and search[y][x] == "A" and checkCrossmasHere(search, x, y):
                print("CrossMAS found at (" + str(x) + ", " + str(y) + ")!")
                totalCrossmas += 1
    return totalCrossmas

def run():
    search = formatSearch(extractInput())
    print(countCrossmas(search))