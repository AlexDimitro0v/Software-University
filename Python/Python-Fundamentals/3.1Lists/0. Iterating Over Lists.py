# Printing a list using a for-loop in Python:

# For-each keeps track only of the elements in the list
lst = ["one", "two", "three", "four", "five", "six"]  # for-each can access only the element
for i in lst:
    print(i, end=" ")

print()
# Printing a list using a string.join(…):
lst = ["one", "two", "three", "four", "five", "six"]
print(", ".join(lst))  # can only join strings

# __________________________________________________________________________________________________________________
# Printing the list and accessing the element and the index
# Normal for-loop keeps track of the elements and the indices
lst = ["one", "two", "three", "four", "five", "six"]
for item in range(0, len(lst)):
    print(lst[item], end=' ')

print()

index = 0
for item in lst:  # works the same
    print(lst[index], end=' ')
    index += 1


# __________________________________________________________________________________________________________________
# Note: there is difference between a list and an array !!!
# https://axiom.utm.utoronto.ca/~207/20f/slides/1/lists-vs-arrays.pdf
