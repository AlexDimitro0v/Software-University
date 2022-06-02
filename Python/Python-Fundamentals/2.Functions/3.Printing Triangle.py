def print_line(start, end):
    for i in range(start, end + 1):  # for-loop from the start(given) up to end(given)
        print(i, end=' ')            # prints on a single line
    print()


def print_triangle(n):
    for i in range(1, n):
        print_line(start=1, end=i)   # calling the function above
    for i2 in range(n, 0, -1):
        print_line(start=1, end=i2)  # calling the function above


print_triangle(int(input()))
