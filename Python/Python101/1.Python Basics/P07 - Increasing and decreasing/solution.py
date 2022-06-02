from enum import Enum


class Monotonicity(Enum):
    INCREASING = 1
    DECREASING = 2
    NONE = 3


def increasing_or_decreasing(ns: list):
    try:
        increasing = False
        decreasing = False
        # https://stackoverflow.com/questions/5764782/iterate-through-pairs-of-items-in-a-python-list
        for previous, current in zip(ns, ns[1:]):
            if previous < current:
                increasing = True
            if previous > current:
                decreasing = True
            if previous == current:
                return Monotonicity.NONE
            
        if (increasing and decreasing) or (not increasing and not decreasing):
            return Monotonicity.NONE
        else:
            if increasing:
                return Monotonicity.INCREASING
            elif decreasing:
                return Monotonicity.DECREASING
    except:
        raise Exception("Incorrect parameter data type was given to the function.")


def increasing_or_decreasing_2(ns: list):
    length = len(ns)
    
    if length <= 1:
        return Monotonicity.NONE

    increasing = True
    decreasing = True
    
    for i in range(length-1):
        previous = ns[i]
        current = ns[i+1]
        increasing = increasing and previous < current
        decreasing = decreasing and previous > current

    if increasing:
        return Monotonicity.INCREASING
    elif decreasing:
        return Monotonicity.DECREASING
    else:
        return Monotonicity.NONE
    
    
if __name__ == '__main__':
    tests = [
        ([1, 2, 3, 4, 5], Monotonicity.INCREASING),
        ([5, 6, -10], Monotonicity.NONE),
        ([1, 1, 1, 1], Monotonicity.NONE),
        ([9, 8, 7, 6], Monotonicity.DECREASING),
        ([], Monotonicity.NONE),
        ([1], Monotonicity.NONE),
        ([1, 100], Monotonicity.INCREASING),
        ([1, 100, 100], Monotonicity.NONE),
        ([100, 1], Monotonicity.DECREASING),
        ([100, 1, 1], Monotonicity.NONE),
        ([100, 1, 2], Monotonicity.NONE),
        ([1, 2, 1, 3], Monotonicity.NONE)
    ]
    
    for test, expected in tests:
        result = increasing_or_decreasing_2(test)
        print(result == expected)
