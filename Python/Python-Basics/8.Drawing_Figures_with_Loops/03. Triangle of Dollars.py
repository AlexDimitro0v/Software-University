# Create a triangle of dollars
def triangle_of_dollars(n):
    for rows in range(1, n+1):
        print("$ " * rows)  # (rows+1)


def triangle_of_dollars2(n):
    for rows in range(n):   # starts from 0
        print("$ " * rows)  # 0 * x = 0 (nothing will be printed on the 1st line)


def triangle_of_dollars3(n):
    for rows in range(1, n+1):
        for column in range(rows):
            print("$", end=' ')
        print()


def main():
    n = int(input())
    triangle_of_dollars(n)


if __name__ == '__main__':
    main()
