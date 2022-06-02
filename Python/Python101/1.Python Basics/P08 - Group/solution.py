"""
Proper way to iterate over a list and change its items with a while loop in-place.
# https://www.quora.com/Why-can%E2%80%99t-you-modify-lists-through-for-in-loops-in-Python
"""


def group(lst: list):
    matrix = []
    length = len(lst)
    index = 0
    
    while index < length:
        current_item_value = lst[index]         # Hold the current item's value
        current_group = [current_item_value]    # Hold the current group
        
        # _______________ PROPER WAY TO ITERATE OVER A LIST WITH A WHILE LOOP ____________
        next_item_index = index+1
        # While not throwing ListIndexOutofRange exception
        # and current_item is equal to next_item
        while next_item_index < length and current_item_value == lst[next_item_index]:
            current_group.append(lst[next_item_index])
            next_item_index += 1
        # ________________________________________________________________________________

        matrix += [current_group]       # equals to .append()
        index = next_item_index
    
    return matrix


def group2(items):
    matrix = []
    for index in range(len(items)):
        item = items[index]
        if not matrix or not matrix[-1][0] == item:
            # If this is the first element or the previous
            # element is not the same as the current one, then add an atomic element
            matrix += [[item]]
        else:
            # If the previous item is equal to the current item, then append
            matrix[-1].append(item)
    return matrix


if __name__ == '__main__':
    tests = [
        ([1, 1, 1, 2, 3, 1, 1], [[1, 1, 1], [2], [3], [1, 1]]),
        ([1, 2, 1, 2, 3, 3], [[1], [2], [1], [2], [3, 3]]),
        ([], []),
        ([1], [[1]]),
        ([1, 1, 1, 1], [[1, 1, 1, 1]])
    ]
    
    for test, expected in tests:
        result = group(test)
        print(result == expected)
