
# Takes data from input as a list
def extractInput():
    with open("/Users/joshtagle/Downloads/advent-2024/input.txt") as file:
        data = list(file)
    for index in range(len(data) - 1):
        data[index] = data[index][:-1]
    return data

# Formats rules and books as lists
def formatRulesAndBooks(data):
    rules = [rule.split("|") for rule in data[:data.index("")]]
    for rulesIndex in range(len(rules)):
        rules[rulesIndex] = [int(rule) for rule in rules[rulesIndex]]
    books = [book.split(",") for book in data[data.index("") + 1:]]
    for booksIndex in range(len(books)):
        books[booksIndex] = [int(book) for book in books[booksIndex]]
    return rules, books

# Checks if given page follows ordering rules
def checkValidPage(rules, book, pageIndex):
    for rule in rules:
        # Implies some following page should be behind
        if rule[1] == book[pageIndex] and rule[0] in book[pageIndex + 1:]:
            return False
        # Implies some previous page should be ahead
        elif rule[0] == book[pageIndex] and rule[1] in book[:pageIndex]:
            return False
    return True

# Checks if all pages in book are valid
def checkValidBook(rules, book):
    for pageIndex in range(len(book)):
        if not checkValidPage(rules, book, pageIndex):
            return False
    return True

# Sums middle pages for all valid books
def sumValidMiddlePages(rules, books):
    sum = 0
    for book in books:
        if checkValidBook(rules, book):
            middlePage = book[int(len(book) / 2)]
            print("Adding valid page " + str(middlePage) + " from book of length " + str(len(book)) + "...")
            sum += middlePage
    return sum

# Finds all rules that order pages in given book
def findRelevantRules(rules, book):
    relevantRules = []
    for rule in rules:
        if set(rule).issubset(set(book)):
            relevantRules.append(rule)
    return relevantRules

# Finds the first valid page of a book from relevant rules
def findFirstPage(relevantRules, book):
    for page in book:
        if not page in [relevantRule[1] for relevantRule in relevantRules]:
            return page

# Returns valid book from its pages and relevant rules
def fixInvalidBook(rules, book):
    relevantRules = findRelevantRules(rules, book)
    validBook = []
    while len(book) > 0:
        firstPage = findFirstPage(relevantRules, book)
        validBook.append(firstPage)
        relevantRules = [relevantRule for relevantRule in relevantRules if relevantRule[0] != firstPage]
        book.remove(firstPage)
    return validBook

# Sums middle pages for all fixed invalid books
def sumInvalidMiddlePages(rules, books):
    sum = 0
    for book in books:
        if not checkValidBook(rules, book):
            book = fixInvalidBook(rules, book)
            middlePage = book[int(len(book) / 2)]
            print("Adding invalid page " + str(middlePage) + " from book of length " + str(len(book)) + "...")
            sum += middlePage
    return sum

def run():
    rules, books = formatRulesAndBooks(extractInput())
    print(sumInvalidMiddlePages(rules, books))