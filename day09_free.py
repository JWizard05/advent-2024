
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
        List of sequential file blocks in disk
        List of file blocks by length
    """

    disk_map = input[0]
    disk = []
    block_list = []
    file_id = 0

    for i, char in enumerate(disk_map):

        if i % 2 == 0:

            block_list.append(int(char))

            for j in range(int(char)):

                disk.append(file_id)

            file_id += 1

        else:

            for j in range(int(char)):

                disk.append(-1)

    return disk, block_list

def find_empty_space(disk, file_id, length):

    """
    Finds a leftward empty space of blocks that can fit a given length
    Parameters:
        (disk): List of sequential file blocks in disk
        (file_id): ID of given file block
        (length): Length of given file block
    Returns:
        Index of free block space
    """

    curr_block = disk.index(file_id)

    for i in range(curr_block - length + 1):

        if all(block == -1 for block in disk[i:i+length]):

            return i

    return -1

def compact_disk(disk, block_list):

    """
    Moves individual file blocks from the end of the disk to the leftmost free space
    Parameters:
        (disk): List of sequential file blocks in disk
        (block_list): List of file blocks by length
    Returns:
        Compacted disk sequence
    """

    for file_id, length in enumerate(block_list[::-1]):

        file_id = len(block_list) - file_id - 1

        curr_block = disk.index(file_id)
        free_block = find_empty_space(disk, file_id, length)

        if free_block > 0:

            print(f"Moving ID {file_id} to position {free_block}...")

            for i in range(length):

                disk[curr_block + i] = -1
                disk[free_block + i] = file_id

    return disk

def run():

    """
    Compacts disk and calculates check_sum value
    Parameters:
        (None)
    Returns:
        (None)
    """

    check_sum = 0

    disk, block_list = parse_input(extract_input())

    disk = compact_disk(disk, block_list)

    for i, block in enumerate(disk):

        if block > 0:

            check_sum += (i * block)

    print(check_sum)