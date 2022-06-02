"""
Write a program that reads from the console a number (radius of a circle) and calculate
the area and perimeter of that circle.
Format the results to the 2nd decimal point.
"""
from math import pi
radius = float(input("Enter r="))


def circle_area(r):
    print(f"Area circle= {pi*r*r:.2f}")
    # print("Area circle= ", pi*r*r)


def circle_perimeter(r):
    print(f"Perimeter circle= {2*pi*r:.2f}")
    # print("Perimeter circle= ", 2*pi*r)


if __name__ == '__main__':
    # This makes the file reusable when dealing with importing
    circle_area(radius)
    circle_perimeter(radius)
