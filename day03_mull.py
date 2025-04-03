
# Takes data from input as a list
def extractInput():
    with open("/Users/joshtagle/Downloads/advent-2024/input.txt") as file:
        data = list(file)
    for index in range(len(data) - 1):
        data[index] = data[index][:-1]
    return data

# Formats memory as string
def formatMemory(data):
    return "".join(data)

# Checks if memory at the current index is valid multiplication function
def checkMul(memory, charIndex):
    currentMemory = memory[charIndex:]
    # Implies multiplication function present
    if currentMemory[:4] == "mul(" and currentMemory.find(")"):
        arguments = currentMemory[4:currentMemory.find(")")].split(",")
        # Implies two integer arguments present
        if all(argument.isdigit() for argument in arguments) and len(arguments) == 2:
            arguments = [int(argument) for argument in arguments]
            return True, arguments
    return False, -1

# Checks if memory at current index allows future multiplication functions
def checkDoOrDont(memory, charIndex, doMul):
    currentMemory = memory[charIndex:]
    if currentMemory[:4] == "do()":
        return True
    elif currentMemory[:7] == "don\'t()":
        return False
    return doMul

# Executes multiplication function
def mul(arguments):
    return arguments[0] * arguments[1]

# Evaluates all functions in memory and sums results
def evaluateMemory(memory):
    result = 0
    doMul = True
    for charIndex in range(len(memory)):
        isMul, arguments = checkMul(memory, charIndex)
        doMul = checkDoOrDont(memory, charIndex, doMul)
        if isMul:
            if doMul:
                print("Found mul(" + str(arguments[0]) + ", " + str(arguments[1]) + ") and executed...")
                result += mul(arguments)
            else:
                print("Found mul(" + str(arguments[0]) + ", " + str(arguments[1]) + ")...")
    return result

def run():
    memory = formatMemory(extractInput())
    print(evaluateMemory(memory))