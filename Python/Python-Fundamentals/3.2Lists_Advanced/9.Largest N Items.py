def main():
    numbers = list(map(int, input().split()))
    numbers.sort(reverse=True)
    count = int(input())
    for times in range(count):
        print(numbers[times], end=" ")

    # print(' '.join([str(n) for n in sorted(numbers, reverse=True)[:count]]))


if __name__ == '__main__':
    main()


