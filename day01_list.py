
# Takes data from input as a list
def extractInput():
    with open("/Users/joshtagle/Downloads/advent-2024/input.txt") as file:
        data = list(file)
    for index in range(len(data) - 1):
        data[index] = data[index][:-1]
    return data

# Formats and sorts lists
def formatLists(data):
    lists = [[], []]
    for line in data:
        lists[0].append(int(line.split("   ")[0]))
        lists[1].append(int(line.split("   ")[1]))
    lists = [sorted(list) for list in lists]
    return lists

# Calculates total distance between corresponding element pairs
def calculateTotalDistance(lists):
    totalDistance = 0
    for lineIndex in range(len(lists[0])):
        distance = abs(lists[0][lineIndex] - lists[1][lineIndex])
        totalDistance += distance
        if distance != 0:
            print("Adding distance of " + str(distance) + "...")
    return totalDistance

# Calculates total similarity score from each element multiplied by adjacent list frequency
def calculateSimilarityScore(lists):
    totalSimilarityScore = 0
    for lineIndex in range(len(lists[0])):
        similarityScore = lists[0][lineIndex] * lists[1].count(lists[0][lineIndex])
        totalSimilarityScore += similarityScore
        if similarityScore != 0:
            print("Adding similarity score of " + str(similarityScore) + "...")
    return totalSimilarityScore

def run():
    lists = formatLists(extractInput())
    print(calculateSimilarityScore(lists))