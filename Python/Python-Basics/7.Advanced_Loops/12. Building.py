"""
Write a program that displays the room numbers in a building (in descending order) following the rules below:
• On every even floor there are only offices - the office numbers are written as follows:
    o "O{floor number}{room number}"
• On every odd floor there are only apartments - the apartment numbers are written as follows:
    o "A{floor number}{room number}"
• Always on the last floor there are large apartments - their numbers are represented as follows:
    o "L{floor number}{room number}"

NOTE: The room numbers start from 0, while the floor numbers start from 1.

Input(reading 2 numbers, one per line):
• The number of floors in the building - int
• The number of rooms on the floors (they are the same for every floor) - int
Output:
• The room numbers representations in descending order

Example:
6 floors and 4 rooms per floor as input:
L60 L61 L62 L63
A50 A51 A52 A53
O40 O41 O42 O43
A30 A31 A32 A33
O20 O21 O22 O23
A10 A11 A12 A13
"""


def is_even(num):
    if num % 2 == 0:
        return True
    return False


def solve(floors, rooms):
    last_floor = floors
    for floor in range(floors, 0, -1):
        for room in range(rooms):
            if floor == last_floor:
                print(f"L{floor}{room}", end=' ')
            else:
                if is_even(floor):
                    print(f"O{floor}{room}", end=' ')
                else:
                    print(f"A{floor}{room}", end=' ')
        print()


def main():
    floors = int(input())
    rooms = int(input())
    solve(floors, rooms)


if __name__ == '__main__':
    main()
