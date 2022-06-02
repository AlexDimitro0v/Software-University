# Multiple Assignment
# https://treyhunner.com/2018/03/tuple-unpacking-improves-python-code-readability/      *AMAZING ARTICLE


# In an assignment statement, the right-hand side is always evaluated fully before doing the actual setting of variable
# Evaluation order matters - here is an example:


def multiple_assignment():
    data_list = [1, 2, 3, 4]
    data_list[0], data_list[1], data_list[2], data_list[3] = data_list[3], data_list[2], data_list[1], data_list[0]
    print(data_list)


def normal_assignment():
    data_list = [1, 2, 3, 4]
    data_list[0] = data_list[3]
    data_list[1] = data_list[2]
    data_list[2] = data_list[1]
    data_list[3] = data_list[0]
    print(data_list)


multiple_assignment()
normal_assignment()


# Another example:
x = 1
y = 2
x, y = y, x+y
print(x, y)

x = 1
y = 2
x = y
y = x+y
print(x, y)

"""
First statement
All variables at the right member are evaluated and, then, are stored in the left members. 
So first proceed with right member, and second with the left member.

In the second statement
x = y
y = x + y
you first evaluate y and assign it to x; 
in that way, the sum of x+y is equivalent to a sum of y+y and not of x+y which is the first case.
"""

