# Create a Diamond
def diamond(n):
    # even number
    if n % 2 == 0:
        range_rows = n//2 - 1
        stars = 2
        dash = (n - stars) // 2
        dash_middle = 2
        print("-"*dash + '*'*stars + "-"*dash)
    # odd number
    else:
        range_rows = n//2
        stars = 1
        dash = (n - stars) // 2
        dash_middle = 1
        print("-" * dash + '*' * stars + "-" * dash)

    for rows in range(1, range_rows+1):
        dash = (n - stars-dash_middle) // 2
        print('-'*dash + '*' + '-'*dash_middle + '*' + '-'*dash)
        dash_middle += 2

    # for the rest of the lines
    dash_middle = n-2
    for rows in range(1, n//2):
        dash_middle -= 2
        dash1 = (n - 2 - dash_middle) // 2
        print('-' * dash1 + '*' + '-' * dash_middle + '*' + '-' * dash1)

    if n % 2 == 1 and not n == 1:
        stars = 1
        dash = (n - stars) // 2
        print("-" * dash + '*' * stars + "-" * dash)


def main():
    n = int(input())
    diamond(n)


if __name__ == '__main__':
    main()
