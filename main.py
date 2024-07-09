def getInput():
    uservalues = input("Please enter list of values: ")
    return list(map(int, uservalues.split()))


def makeReverse(numbers):
    result = []
    """
    # using insert method
    for elem in numbers:
        result.insert(0, elem)
    """

    # using pop/append methods
    while len(numbers) > 0:
        result.append(numbers.pop())

    return result


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f"The result values are: {ret}")


if __name__ == "__main__":
    main()
