def find_min(numbers):
    smallest = int(numbers[0])
    for elem in numbers:
        if int(elem) < smallest:
            smallest = int(elem)

    return smallest


def find_min2(numbers):
    try:
        numbers = map(int, numbers)
        min_number = min(numbers)
    except ValueError:
        return "No numbers provided."
    return min_number


def main():
    numbers = input().split()
    print(find_min2(numbers))


def min_description():
    print(help(min))


if __name__ == '__main__':
    main()
