# Write a simple program to convert inches to cm. Format the cm to the 2nd decimal point.
def inches_to_cm(inches):
    cm = inches * 2.54
    # print (inches, "Inches are", cm, "cm")
    return f"{cm:.2f}"


if __name__ == '__main__':
    print(inches_to_cm(inches=float(input("Inches: "))))
