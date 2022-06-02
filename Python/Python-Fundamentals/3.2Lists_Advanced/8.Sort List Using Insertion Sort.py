def insertion_sort1(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i-1]:
            for j in range(i):
                if lst[i] < lst[j]:
                    lst[i], lst[j] = lst[j], lst[i]


# ________________________________________________________________
# another way
def insertion_sort2(numbers):
    for i in range(1, len(numbers)):
        current = i
        while True:
            if current == 0:
                break
            f_num = numbers[current-1]
            s_num = numbers[current]
            if s_num < f_num:
                numbers[current], numbers[current-1] = numbers[current-1], numbers[current]  # swapping the elements
                current = current-1
            else:
                break


# ________________________________________________________________
# Function to do insertion sort
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        current = arr[j]
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


def main():
    numbers = list(map(int, input().split()))
    insertion_sort2(numbers)
    print(" ".join(map(str, numbers)))


if __name__ == '__main__':
    main()

