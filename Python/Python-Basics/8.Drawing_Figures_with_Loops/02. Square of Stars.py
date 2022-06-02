# Create a square of stars
def square_of_stars(n):
    for row in range(n):
        print("*"*n)


def main():
    n = int(input())
    square_of_stars(n)


if __name__ == '__main__':
    main()
