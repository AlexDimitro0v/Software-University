# List slicing:
# a[start:stop]  # items start through stop-1
# a[start:]      # items start through the rest of the array
# a[:stop]       # items from the beginning through stop-1
# a[:]           # a copy of the whole array


def balanced_numbers(number: int):
    """
    A function created by Alex to calculate if left and right parts of a number are equal.
    """
    try:
        number_len = len(str(number))
        is_balanced = False
        split_index = number_len//2     # middle (rounded down by the floor division operator)
        if number_len % 2 == 0:
            # no middle (i.e. even number of digits)
            first_half = list(map(int, str(number)[:split_index]))
            second_half = list(map(int, str(number)[split_index:]))
            if sum(first_half) == sum(second_half):
                is_balanced = True
        else:
            # odd number of digits
            first_half = list(map(int, str(number)[:split_index]))
            second_half = list(map(int, str(number)[split_index+1:]))
            if sum(first_half) == sum(second_half):
                is_balanced = True
        
        return is_balanced
    
    except:
        raise Exception("Incorrect parameter data type was given to the function.")


def is_number_balanced(number):
    #  0  1    2  3
    # [4, 5, | 1, 8] -> even length
    # -----
    #  0  1  2   3   4  5  6
    # [1, 2, 3, |8|, 0, 3, 3] -> odd length
    digits = list(map(int, str(abs(number))))
    length = len(digits)
    middle = length // 2          # mid_split_index
    is_odd_length = length % 2 == 1
    
    left_sum = 0
    right_sum = 0
    
    for index, digit in enumerate(digits):
        if index < middle:
            left_sum += digit
        else:
            if index == middle and is_odd_length:
                continue
            
            right_sum += digit
    
    return left_sum == right_sum


def is_number_balanced_2(number):
    numbers_list = [int(n) for n in str(number)]
    mid_index = len(numbers_list) // 2
    left_sum = sum(numbers_list[:mid_index])
    if not len(numbers_list) % 2 == 0:
        mid_index += 1
    right_sum = sum(numbers_list[mid_index:])
    return left_sum == right_sum


if __name__ == '__main__':
    tests = [
        (9, True),
        (4518, True),
        (1111, True),
        (11111, True),
        (28471, False),
        (1238033, True),
        (123, False),
        (121, True),
    ]
    
    for test, expected in tests:
        result = is_number_balanced(test)
        print(result == expected)

