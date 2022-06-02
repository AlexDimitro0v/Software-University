"""
Write a program that reads n number of integers (n>0) entered by the user and finds the biggest among them.

Input:
• First Line - n (the number of integers to be entered from the user).
• The next n lines - a single integer per line.
Output:
• The biggest number
Example:
    Input               Output
       3
      20
      -4
      10                  20
"""


def solve(n):
    max_number = float('-inf')             # the smallest number (-infinity)
    # min_number = float('inf')            # the biggest number (infinity)

    for number in range(n):
        number_input = int(input())

        if number_input > max_number:
            max_number = number_input

    print("max =", max_number)


def main():
    print("n = ", end="")        # \n newline; end='' leaves the cursor on the same line
    solve(int(input()))


if __name__ == '__main__':
    main()
