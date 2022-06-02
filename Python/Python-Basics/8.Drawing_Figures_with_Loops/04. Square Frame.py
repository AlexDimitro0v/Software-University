# Create a square frame
def square_frame(n):
    print("+ " + "- " * (n - 2) + "+")
    for rows in range(1, (n - 2)+1):
        print("| " + "- " * (n - 2) + "|")

    print("+ " + "- " * (n - 2) + "+")


# Given: n*n => height: n     length: n
# Static: first and last rows:
# + '+' ... '-'  *(n-2) times....'+'
# rest of the lines: for-loop in range (1, n-1)


def main():
    n = int(input())
    square_frame(n)


if __name__ == '__main__':
    main()
