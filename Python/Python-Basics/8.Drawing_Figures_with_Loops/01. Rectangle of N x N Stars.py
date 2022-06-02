# Create a rectangle of stars
def rectangle_of_stars(n):
    for row in range(n):
        print("*" * n)


def main():
    n = int(input())
    rectangle_of_stars(n)


if __name__ == '__main__':
    main()
