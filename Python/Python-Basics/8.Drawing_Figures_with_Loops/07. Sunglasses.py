# Create Sunglasses
def sunglasses(n):
    stars = 2*n
    space = 5*n - 4*n
    slash = 2*n - 2                                             # because of the 2 static symbols (the 2 stars)

    print('*' * stars + ' '*space + '*' * stars)                # static line

    for rows in range(1, n-1):                                  # (1, (n-2)+1)
        if rows == n//2 and not n % 2 == 0:
            print('*' + '/' * slash + '*' + '|' * space + '*' + '/' * slash + '*')
        elif rows == (n//2) - 1 and n % 2 == 0:
            print('*' + '/' * slash + '*' + '|' * space + '*' + '/' * slash + '*')
        else:
            print('*' + '/' * slash + '*' + ' ' * space + '*' + '/' * slash + '*')

    print('*' * stars + ' '*space + '*' * stars)                # static line

    # size of the sunglasses (5*n x n) -> 5*n(length) и n(height)
    # static rows
    # * -> 2*n
    # ' ' -> 5*n - (2*n + 2*n = 4*n) or 5*n - 4*n or just n
    # * -> 2*n


def main():
    n = int(input())
    sunglasses(n)


if __name__ == '__main__':
    main()
