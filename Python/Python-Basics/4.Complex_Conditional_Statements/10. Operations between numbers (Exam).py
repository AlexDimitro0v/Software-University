# 26th March 2016 - SoftUni exam question.
"""
Input:
• N1 - integer in range (0...40 000)
• N2 - integer in range (0...40 000)
• Operator - one character among: "+", "-", "*", "/", "%"

Output(Print a single line on the console):
• If the operation is a addition, subtraction, or multiplication:
    o "{N1} {operator} {N2} = {result} - {even/odd}"  Should display if the result is even or odd.
• If the operation is a division:
    o "{N1} / {N2} = {result}" - the result is formatted to the 2nd decimal number.
• If the operation is a modular division:
    o {n1} % {N2} = {remainder}
• In the case of division by 0(zero):
    o "Can not divide {N1} by zero"
"""


def make_operation(operator, n1, n2):
    if operator == "/":
        if n2 == 0:
            result = f"Cannot divide {n1} by zero"
        else:
            operation = n1 / n2
            result = "{} / {} = {}".format(n1, n2, "%.2f" % operation)

    elif operator == "%":
        if n2 == 0:
            result = f"Cannot divide {n1} by zero"
        else:
            operation = n1 % n2
            result = f"{n1} % {n2} = {operation}"

    elif operator == "+" or operator == "-" or operator == "*":
        if operator == "+":
            operation = n1 + n2
        elif operator == "-":
            operation = n1 - n2
        elif operator == "*":
            operation = n1 * n2
        if operation % 2 == 0:
            result = f"{n1} {operator} {n2} = {operation} - even"
        else:
            result = f"{n1} {operator} {n2} = {operation} - odd"
    else:
        print("Error.")
        return

    return result


def main():
    n1 = int(input())
    n2 = int(input())
    operator = input()
    print(make_operation(operator, n1, n2))


if __name__ == '__main__':
    main()

