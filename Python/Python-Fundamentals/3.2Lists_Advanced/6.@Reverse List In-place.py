# Reverse a list in-place, i.e
# as in, don’t create a new collection to hold the result, reverse it using only the original list.


def reverse_in_place(lst):
    for i in range(0, int(len(lst)/2)):
        lst[i], lst[i-1 - 2*i] = lst[i-1 - 2*i], lst[i]

    print(*lst, sep=" ")


def main():
    numbers = list(map(int, input().split()))
    """
    The description of the task does NOT allow this:
    for elem in numbers[::-1]:
        print(elem, end=' ')
    """
    numbers.reverse()              # there is already a python built-in for the purpose
    for elem in numbers:
        print(elem, end=" ")


if __name__ == '__main__':
    main()

