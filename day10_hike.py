
def extract_input():

    """
    Extracts input from input file
    Parameters:
        (None)
    Returns:
        List of lines from input file
    """

    with open("/Users/joshtagle/Downloads/advent-2024/input.txt") as file:

        input = list(file)

    for index in range(len(input) - 1):

        input[index] = input[index][:-1]

    return input

def parse_input(input):

    """
    Parses input into list representation
    Parameters:
        (input): List of lines from input file
    Returns:
        2-dimensional list of positions as a topological map
        List of trailhead coordinates
    """

    map = ([[int(position) for position in row] for row in input])
    trailheads = []

    for y in range(len(map)):

        for x in range(len(map[0])):

            if map[y][x] == 0:

                trailheads.append([x, y])

    return map, trailheads

def count_mountains(map, curr_position, next_value):

    """
    Uses recursion to count unique, ascending paths from the current position to a mountain
    Parameters:
        (map): 2-dimensional list of positions as a topological map
        (curr_position): Coordinates of current position
        (next_value): Expected value of next step
    Returns:
        Number of unique paths to a mountain
    """

    count = 0

    curr_x, curr_y = curr_position

    print(f"{curr_x} {curr_y}")

    if map[curr_y][curr_x] != next_value:

        return 0

    if map[curr_y][curr_x] == 9:

        return 1
    
    if curr_x > 0:

        count += count_mountains(map, [curr_x - 1, curr_y], next_value + 1)

    if curr_x < (len(map[0]) - 1):

        count += count_mountains(map, [curr_x + 1, curr_y], next_value + 1)

    if curr_y > 0:

        count += count_mountains(map, [curr_x, curr_y - 1], next_value + 1)

    if curr_y < (len(map) - 1):

        count += count_mountains(map, [curr_x, curr_y + 1], next_value + 1)

    return count

def run():

    """
    Sums the unique, ascending paths from each trailhead to a mountain
    Parameters:
        (None)
    Returns:
        (None)
    """

    map, trailheads = parse_input(extract_input())

    count = 0

    for trailhead in trailheads:

        map_copy = [row[:] for row in map]

        count += count_mountains(map_copy, trailhead, 0)

    print(count)