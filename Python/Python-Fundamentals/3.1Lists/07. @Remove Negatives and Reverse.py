def remove_negatives_and_reverse(lst):
    """
    :param   lst:    a list
    :return: no returning value - modifies the list in-place
    """
    # lst = [x for x in lst if int(x) >= 0]             # 1.List Comprehension solution
    # lst = list(filter(lambda x: int(x) >= 0, lst))    # 2.Filter Built-In solution
    # (Both do NOT modify the list in place i.e both methods create a new list)

    for i in lst[:]:                                    # 3.List Slicing solution
        # Optimal Solution(Best performance) - modifies the list in place
        if int(i) < 0:
            lst.remove(i)

    lst.reverse()           # the reverse function is void (with no return value, i.e prints None)
    # Note: The in-place built-in methods do not return anything


# another way
def solve():
    numbers = [int(n) for n in input().split(' ')]
    positives = [number for number in numbers if number >= 0]
    result = ' '.join([str(x) for x in positives[::-1]]) if positives else 'empty'
    print(result)


def main():
    lst = input().split()  # split creates a list of integers
    remove_negatives_and_reverse(lst)
    if len(lst) == 0:         # or if no lst:
        print("empty")

    print(' '.join(lst))


if __name__ == '__main__':
    main()

# NOTE: Filter and map return generators - more for generators here:
# https://www.youtube.com/watch?v=bD05uGo_sVI
