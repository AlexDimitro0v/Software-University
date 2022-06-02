# Write a simple program to convert celsius to fahrenheit.
# Format the result to the 2nd decimal point.
celsius = float(input("Enter celsius: "))


def celsius_to_fhr(cls):
    fahrenheit_convert = cls * 1.8 + 32
    return fahrenheit_convert


if __name__ == '__main__':
    print("%.2f" % celsius_to_fhr(celsius) + 'F')
