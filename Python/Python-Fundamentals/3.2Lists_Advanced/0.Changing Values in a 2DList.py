values = [[10, 0], [13, 0], [36, 0], [74, 0], [22, 0]]
whatever = 5

# printing the values list
for lst in values:                  # for all lists
    for element in lst:             # for all elements from all lists
        print(element, end=' ')
    print()
# print(values)


# changing the second element of every inner list
def changing_the_2d_list(collection):
    for array in collection:
        array[1] = array[0] + whatever


changing_the_2d_list(values)
print(*values, sep='; ')
