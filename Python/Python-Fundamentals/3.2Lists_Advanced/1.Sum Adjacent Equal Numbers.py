# Solvable with a while loop
def sum_adjacent_equal_numbers(numbers):               # naive solution
    counter = 0
    while counter < len(numbers) - 1:
        # len_checker = len(numbers) - 1               # debugging to see how it iterates over all indices

        first_number = numbers[counter]
        second_number = numbers[counter+1]

        if first_number == second_number:
            numbers[counter] = numbers[counter] + numbers[counter+1]    # first_number = first_number+second_number
            numbers.pop(counter+1)
            counter -= 1
            if counter < 0:
                counter = 0
        else:
            counter += 1
    # print(numbers)


# ______________________________________________________________________________
# another way
def sum_adjacent_equal_numbers2(lst):
    found = True

    while found:
        found = False
        for n in range(0, len(lst)-1):
            if lst[n] == lst[n+1]:
                lst[n] = lst[n] + lst[n+1]
                lst.pop(n+1)
                found = True
                break


def main():
    numbers = list(map(float, input().split()))
    sum_adjacent_equal_numbers(numbers)
    for i in numbers:
        print(f"{i:.2g}", end=' ')         # general formatting
    # https://stackoverflow.com/questions/1742937/convert-float-to-string-with-cutting-zero-decimals-afer-point-in-python


if __name__ == '__main__':
    main()
