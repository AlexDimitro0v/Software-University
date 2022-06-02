def contains(numbers, n):
    if n in numbers:
        return True
    return False


def main():
    numbers = list(map(int, input().split()))
    n = int(input())
    if contains(numbers, n):
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    main()

