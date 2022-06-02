def generate_sequence(start, end, step):
    for num in range(start, end, step):            # try with 20,-20,-2 and -20,20,2
        print(num)


def main():
    start = int(input())
    end = int(input())
    step = int(input())
    generate_sequence(start, end, step)


if __name__ == '__main__':
    main()
