"""Taking the sides of a rectangle as inputs - a and b, compute the area of the rectangle"""


def user_input():
    side_a = int(input("Give a number: "))
    side_b = int(input("Give a number: "))
    return side_a, side_b


a, b = user_input()                     # The Pythonic way of unpacking
print("a x b = ", a * b, " cm")
print("a x b = " + str(a * b) + " cm")  # The same as the line above
