"""
Write a program that outputs all 2x2 matrices that satisfy the following conditions:
• The elements on the first row are in the interval [a:b] and the elements of the the second row are in the interval
[c:d]
• The sum of the elements of the main diagonal is equal to the sum of elements of the secondary diagonal
• No identical elements on 1 line   e.g 22 is not permitted

Input(reading 4 numbers, one per line):
• a,b,c,d - the intervals' range
Output:
• All the matrices that satisfy the conditions above and lie in the given interval
"""


def solve(a, b, c, d):
    for first_row_first_num in range(a, b+1):
        for first_row_second_num in range(a, b+1):
            for second_row_first_num in range(c, d+1):
                for second_row_second_num in range(c, d+1):
                    if first_row_first_num+second_row_second_num == first_row_second_num+second_row_first_num:
                        if first_row_first_num != first_row_second_num and second_row_first_num != second_row_second_num:
                            print(f"{first_row_first_num    }{first_row_second_num}")
                            print(f"{second_row_first_num}{second_row_second_num}\n")
                            # print()


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    solve(a, b, c, d)


if __name__ == '__main__':
    main()
