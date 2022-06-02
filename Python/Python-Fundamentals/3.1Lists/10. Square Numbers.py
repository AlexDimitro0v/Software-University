import math


def square_numbers(number):
    if number > 0 and math.sqrt(number) == int(math.sqrt(number)):
        return True
    return False


def main():
    # Filter Solution: https://www.geeksforgeeks.org/filter-in-python/
    lst = [int(item) for item in input().split()]                 # default splitting symbol is empty string
    filtered = sorted(filter(square_numbers, lst), reverse=True)  # reverses the list in an descending order
    print(' '.join(map(str, filtered)))


if __name__ == '__main__':
    main()
