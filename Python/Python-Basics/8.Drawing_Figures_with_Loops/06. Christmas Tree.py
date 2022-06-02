# Create a Christmas Tree
def christmas_tree(n):
    for rows in range(n+1):
        print(" "*(n-rows) + "*" * rows + " | " + "*" * rows)

# the for loop should be in range(0, n+1) so that we can print the stars properly
# spaces = n-rows
# stars = rows times
# static symbol " | "
# stars again = rows times


def christmas_tree2(n):
    print(" " * n + ' | ' + " "*n)      # static line

    for rows in range(1, n+1):         # dynamic line
        print(" "*(n-rows) + "*"*rows + ' | ' + "*"*rows)


def main():
    n = int(input())
    christmas_tree(n)


if __name__ == '__main__':
    main()

