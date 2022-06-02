def count_odds(lst):
    map(int, lst)
    """
    :param lst:  a list of integers
    :return:     the number of odd numbers
    """
    count = 0
    # Odd numbers, which are negative, have a remainder of -1.
    for number in lst:
        if number % 2 == 1 or number % 2 == -1:
            count += 1
    return count


print(count_odds(lst=input().split(' ')))
# if number % 2 != 0          catches all odd numbers(incl.negative ones) /// another possibility is to use abs()
