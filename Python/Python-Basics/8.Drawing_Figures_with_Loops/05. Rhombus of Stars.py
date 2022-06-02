def rhombus_of_stars(n):
    for rows in range(1, n+1):
        print(" " * (n - rows) + "* " * rows)

    for rows in range(1, n):
        print(" " * rows + "* " * (n - rows))

# Divide the figure to upper and lower part
# UPPER Part:
# spaces   = (n-rows)
# the star = '* ' times rows time for every row

# LOWER Part (n-1 times):
# spaces   = rows times
# the star = n-rows


def rhombus_of_stars2(n):
    space = " "
    star = "* "
    second_part_star = n - 1
    for rows in range(1, (2*n-1)+1):
        if rows <= n:
            print(space * (n-rows) + star*rows)
        else:
            print(space * (rows-n) + star*second_part_star)
            second_part_star -= 1  # decrementing the variable


def main():
    n = int(input())
    rhombus_of_stars(n)


if __name__ == '__main__':
    main()
