"""
Given a coordinate system, a rectangle is set with the coordinates of two of its opposite angles (x1, y1) - (x2, y2).
Calculate the area and the perimeter of this rectangle. Format the results to the 2nd decimal point.
Input:
x1, y1, x2, y2
Output:
1.The area
2.The perimeter
"""

x1 = float(input("Give me a number for x1: "))
y1 = float(input("Give me a number for y1: "))
x2 = float(input("Give me a number for x2: "))
y2 = float(input("Give me a number for y2: "))


def rectangle_coordinate_data(x1, y1, x2, y2):
    a = abs(x1 - x2)
    b = abs(y1 - y2)

    area = a * b
    perimeter = 2 * (a + b)
    print(f"{area:.2f}")
    print(f"{perimeter:.2f}")


def rectangle_data_from_coordinates(x1, y1, x2, y2):
    width = max(x1, x2) - min(x1, x2)   # a    takes the higher from x1;x2 and subtracts the lower from x1;x2
    height = max(y1, y2) - min(y1, y2)  # b
    print(f"Area= {width * height:.2f}")             # Area=a*b
    print(f'Perimeter= {2 * (width + height):.2f}')  # Perimeter = 2*(a+b)


if __name__ == '__main__':
    rectangle_coordinate_data(x1, y1, x2, y2)
