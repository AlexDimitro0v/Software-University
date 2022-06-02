"""
Write a console program that finds the greater number between 2 given numbers and prints it.
"""


def greater(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


if __name__ == '__main__':
    number1 = int(input("Give me a whole number: "))
    number2 = int(input("Give me another whole number: "))
    print("Greater number: " + str(greater(number1, number2)))
