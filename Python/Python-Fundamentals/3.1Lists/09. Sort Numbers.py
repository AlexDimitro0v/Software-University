def print_sorted_numbers():
    values = input()
    items = values.split()
    nums = []

    for i in items:
        nums += [int(i)]

    nums.sort()                        # Python uses TimSort as a built-in.

    # Common Python Gotcha:
    # print(nums.index(nums[-1]))      if we have 1 2 3 3 3 will return the index of the first of the repeated elements
    # print(len(nums)-1)               always returns the index of the very last list element
    for number in range(len(nums)):
        if number == len(nums)-1:              # nums.index(nums[-1])  won't work if we enter 1 2 3 3
            print(f"{nums[number]}")
        else:
            print(f"{nums[number]} <= ", end='')

    # print(' <= '.join(map(str, nums)))        simpler way to do the same


# __________________________________________
# another way
def print_sorted_numbers2():
    values = input()
    list1 = values.split(' ')

    # cast the list to integers
    list1 = list(map(int, list1))
    list1 = sorted(list1)
    list2 = list1.pop()

    # for j in list1:
    #      print(str(j) + ' <= ', end = '')

    print(' <= '.join(map(str, list1)), end=' <= ')
    print(list2)


def main():
    # Two-Liner:
    data = sorted(list(map(int, input().split(' '))))
    print(' <= '.join(map(str, data)))


if __name__ == '__main__':
    main()
