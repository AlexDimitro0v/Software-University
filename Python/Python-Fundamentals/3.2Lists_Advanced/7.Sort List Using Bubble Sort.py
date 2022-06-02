# comparison of all sorting algorithms:
# https://www.youtube.com/watch?v=YHm_4bVOe1s&list=PLj8W7XIvO93rJHSYzkk7CgfiLQRUEC2Sq&index=3


def bubble_sort1(numbers):
    swapped = True              # In order to enter the while loop
    end = len(numbers)-1

    while swapped:              # while True
        swapped = False
        for i in range(end):
            first_number = numbers[i]
            second_number = numbers[i + 1]

            if first_number > second_number:
                # temp_item = list[i]   # Keep the current element
                # list[i] = list[i+1]   # Swap elements
                # list[i+1] = temp_item # Swap elements

                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]  # swap(left_element, right_element)
                swapped = True


# _______________________________________________________________________
# Super useful for debugger
def bubble_sort2(lst):
    for e in range(len(lst)-1, 0, -1):
        for i in range(e):
            if lst[i] > lst[i+1]:
                lst[i+1], lst[i] = lst[i], lst[i+1]


# ______________________________________________________________________
# another way
def bubble_sort3(mylist):
    for i in range(0, len(mylist)-1):
        for j in range(0, len(mylist)-1-i):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]


def main():
    numbers = list(map(int, input().split()))
    bubble_sort2(numbers)
    print(" ".join(map(str, numbers)))

    # use of the help function
    # print(help(list.sort))
    # print(help(sorted))


if __name__ == '__main__':
    main()
