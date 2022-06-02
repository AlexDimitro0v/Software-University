# Create a figure of a house
def house(n):
    if n % 2 == 0:
        range_rows = n // 2
        stars = 2
    else:
        range_rows = n // 2 + 1
        stars = 1

    dash = (n-stars) // 2        # to take the both sides (left and right), you have to do a integer division by 2

    # for the roof
    for rows in range(0, int(range_rows)):
        print('-' * dash + '*'*stars + '-' * dash)
        stars += 2
        dash = (n - stars) // 2                     # or dash -= 1

    # for the base
    other_rows = n - range_rows
    for rows in range(0, int(other_rows)):
        print('|' + '*'*(n-2) + '|')


def house2(n):
    stars_even = 2
    stars_odd = 1

    if n % 2 == 0:
        for rows1 in range(1, int(n // 2 + 1)):
            dash1 = (n-stars_even) // 2
            print('-' * dash1 + '*'*stars_even+'-'*dash1)
            stars_even += 2
    else:
        for rows1 in range(1, int(n // 2 + 2)):
            dash1 = (n - stars_odd) // 2
            print('-'*dash1 + '*'*stars_odd + '-'*dash1)
            stars_odd += 2

    rows2 = n - rows1

    for rows in range(1, rows2+1):
        print('|' + '*'*(n-2)+'|')


def main():
    n = int(input())
    house(n)


if __name__ == '__main__':
    main()



