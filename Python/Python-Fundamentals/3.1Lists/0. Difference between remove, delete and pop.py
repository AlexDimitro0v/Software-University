# https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists
# pop() and del remove elements by index
# remove        removes elements by value
"""
pop()  - Takes Index and returns Value  (default value to be removed is the last element of the list)
delete - Takes Index, removes value at that index, and returns nothing
remove - Takes Value, removes first occurrence, and returns nothing
"""

# remove  - removes the first matching value, NOT a specific index:
a = [0, 2, 3, 2]
a.remove(2)
print(a)    # [0, 3, 2]


# del  - removes the item at a specific index:
b = [3, 2, 2, 1]
del b[1]
print(b)    # [3, 2, 1]

# del (unlike pop) allows the removal of a range of indexes because of list slicing:
lst = [3, 2, 2, 1]
del lst[1:]
print(lst)  # [3]


# pop - removes the item at a specific index and returns it.
c = [4, 3, 5]
c.pop(1)
print(c)    # [4, 5]
