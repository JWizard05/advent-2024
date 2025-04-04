
from itertools import combinations

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
    Parses input into dictionary representation
    Parameters:
        (input): List of lines from input file
    Returns:
        Input in form {satellite_or_antinode: [coordinates_list]}
        List of frequencies
        Map dimensions
    """

    map = [list(line) for line in input]
    frequencies = list(set([element for row in map for element in row]))

    nodes = {}
    frequencies.remove(".")

    for frequency in frequencies:

        nodes[frequency] = []
        nodes[frequency + "#"] = []

    for y in range(len(map)):

        for x in range(len(map[0])):

            if map[y][x] in frequencies:

                nodes[map[y][x]].append([x, y])

            dimensions = [x, y]
    
    return nodes, frequencies, dimensions

def get_antinodes(pair, dimensions):

    """
    Plots and returns antinodes within bounds reflecting between the given satellite pair
    Parameters:
        (pair): List of two antinode coordinates
        (dimensions): Map size
    Returns:
        Antinode coordinates within the map
    """

    node_one, node_two = pair

    x_diff = node_two[0] - node_one[0]
    y_diff = node_two[1] - node_one[1]

    antinodes = []
    
    x_curr = node_one[0] + x_diff
    y_curr = node_one[1] + y_diff

    while 0 <= x_curr <= dimensions[0] and 0 <= y_curr <= dimensions[0]:

        antinodes.append([x_curr, y_curr])
        x_curr += x_diff
        y_curr += y_diff

    x_curr = node_two[0] - x_diff
    y_curr = node_two[1] - y_diff

    while 0 <= x_curr <= dimensions[0] and 0 <= y_curr <= dimensions[0]:

        antinodes.append([x_curr, y_curr])
        x_curr -= x_diff
        y_curr -= y_diff

    return antinodes

def count_unique_antinodes(nodes, frequencies):

    """
    Counts the number of unique antinodes
    Parameters:
        (nodes): Dictionary in form {satellite_or_antinode: [coordinates_list]}
        (frequencies): List of frequencies
    Returns:
        Unique antinode count
    """

    antinodes = []

    for frequency in frequencies:

        antinodes += nodes[frequency + "#"]

    return len(set(tuple(antinode) for antinode in antinodes))

def run():

    """
    Sums unique antinodes from each satellite combination with the same frequency
    Parameters:
        (None)
    Returns:
        (None)
    """

    nodes, frequencies, dimensions = parse_input(extract_input())

    for frequency in frequencies:

        pairs = list(combinations(nodes[frequency], 2))

        for pair in pairs:

            nodes[frequency + "#"] += get_antinodes(pair, dimensions)

        print(f"Parsed {len(nodes[frequency + "#"])} antinodes for frequency {frequency}...")

    print(count_unique_antinodes(nodes, frequencies))