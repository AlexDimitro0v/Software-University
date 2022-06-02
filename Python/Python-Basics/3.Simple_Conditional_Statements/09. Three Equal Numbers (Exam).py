"""
Read unknown number of integers. Output "yes" if they have the same value or "no" otherwise.
"""


def equality(*args):
    for item in args[1:]:
        if args[0] != item:
            return False
    return True


if __name__ == '__main__':
    one = int(input())
    two = int(input())
    three = int(input())
    if equality(one, two, three):
        print("yes")
    else:
        print("no")
