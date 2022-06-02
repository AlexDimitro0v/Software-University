# Write a simple program to convert radians to degrees. Round the result.
from math import pi
user_input = float(input("Enter an angle in radians: "))


def radians_to_degrees(radians):
    degrees = radians*180/pi
    return degrees


if __name__ == '__main__':
    print("Radians to degrees:", round(radians_to_degrees(user_input)))
