
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
        Input in form [target_value, arguments_list]
    """

    for i, equation in enumerate(input):

        target_value = int(equation.split(": ")[0])
        arguments = [int(argument) for argument in equation.split(": ")[1].split(" ")]
        input[i] = [target_value, arguments]
    
    return input

def attempt_equation(current_value, target_value, next_arguments, history):

    """
    Recursively attempts to add, multiply, and concatenate each following argument until target_value reached
    Parameters:
        (current_value): Value of previous operations
        (target_value): Desired value
        (next_arguments): List of following values
        (history): List of operators tried
    Returns:
        List of operators that yield target_value
    """

    if current_value == target_value and len(next_arguments) == 0:
        return history

    if not next_arguments:
        return []

    add_result = attempt_equation(current_value + next_arguments[0], target_value, next_arguments[1:], history + ["+"])

    if len(add_result) != 0:
        return add_result

    mult_result = attempt_equation(current_value * next_arguments[0], target_value, next_arguments[1:], history + ["*"])

    if len(mult_result) != 0:
        return mult_result
    
    concat_result = attempt_equation(int(str(current_value) + str(next_arguments[0])), target_value, next_arguments[1:], history + ["||"])

    return concat_result

def print_solution(target_value, history):

    """
    Prints the solution opreators
    Parameters:
        (target_value): Desired value
        (history): List of operators that yield target_value
    Returns:
        (None)
    """
    
    print(f"Confirmed {target_value} using {history}...")
    
def run():

    """
    Attempts to solve each equation, prints the solution, and counts the number of successes
    Parameters:
        (None)
    Returns:
        (None)
    """

    input = parse_input(extract_input())

    calibration_result = 0

    for equation in input:
        
        target_value = equation[0]
        arguments_list = equation[1]

        current_value = arguments_list[0]
        next_arguments = arguments_list[1:]

        solution = attempt_equation(current_value, target_value, next_arguments, [])
        
        if len(solution) > 0:
            print_solution(target_value, solution)
            calibration_result += target_value

    print(calibration_result)
