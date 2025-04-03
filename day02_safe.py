
# Takes data from input as a list
def extractInput():
    with open("/Users/joshtagle/Downloads/advent-2024/input.txt") as file:
        data = list(file)
    for index in range(len(data) - 1):
        data[index] = data[index][:-1]
    return data

# Formats reports as lists
def formatReports(data):
    reports = [list(report.split(" ")) for report in data]
    for reportIndex in range(len(reports)):
        reports[reportIndex] = [int(level) for level in reports[reportIndex]]
    return reports

# Checks if a report meets safety standards
def checkSafety(report):
    # Implies report is in ascending or descending order
    if not (report == sorted(report) or report == sorted(report)[::-1]):
        print("Caught failed report for inconsistent ordering...")
        return False
    # Implies report has no repeat elements
    if len(report) != len(set(report)):
        print("Caught failed report for repeated element...")
        return False
    # Implies distance between consecutive elements is within limit
    for levelIndex in range(len(report) - 1):
        difference = abs(report[levelIndex] - report[levelIndex + 1])
        if difference > 3:
            print("Caught failed report for extreme difference of " + str(difference) + "...")
            return False
    return True

# Checks if any report missing some element meets safety standards
def checkDampenedSafety(report):
    for levelIndex in range(len(report)):
        if checkSafety(report[:levelIndex] + report[levelIndex + 1:]):
            return True
    return False

# Counts number of reports that meet safety standards
def countSafeReports(reports):
    safeReportCount = 0
    for report in reports:
        if checkDampenedSafety(report):
            safeReportCount += 1
    return safeReportCount

def run():
    reports = formatReports(extractInput())
    print(countSafeReports(reports))