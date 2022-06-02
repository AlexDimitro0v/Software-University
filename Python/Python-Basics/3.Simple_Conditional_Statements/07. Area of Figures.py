"""
Write a program that introduces the dimensions/sizes of a geometric figure and calculates its area.
The figures are four types: square, rectangle, circle, and triangle. The first line of the input reads the type of the
figure (square, rectangle, circle or triangle).
If the figure is a square, the next line reads one number - the length of its side.
If the figure is a rectangle, the next two lines read two numbers - the lengths of its sides.
If the figure is a circle, the next line reads one number - the radius of the circle.
If the figure is a triangle, the next two lines read two numbers - the length of its side and the length of its height.
Round the result to 3 decimal point.
"""
# Algorithm:
# 1. Read figure type
# 2. Check if:
#   a: square -> read "a"
#   b: rectangle -> read width and length
#   c: circle -> read radius
#   d: triangle -> read "a" and ha
import math


def calculate_figure_area(figure):
    if figure == "square":
        a = float(input())
        return a**2

    elif figure == "rectangle":
        width = float(input())
        length = float(input())
        return width*length

    elif figure == "circle":
        radius = float(input())
        return math.pi * radius**2  # pi * r * r   (pi should be used with the exact value)

    elif figure == "triangle":
        side = float(input())
        height = float(input())
        return side * height / 2


if __name__ == '__main__':
    figure_type = input("Enter the figure: ")
    area = calculate_figure_area(figure_type)
    print("%.3f" % area)
    # print(f"The area is : {area}")
