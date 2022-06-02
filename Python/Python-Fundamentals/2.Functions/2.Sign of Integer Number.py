def sign(number):
    # Function to check the sign of a number
    """
    :param   number: number types
    :return: text:   string
    """
    if number > 0:
        print(f"The number {number} is positive.")
    elif number < 0:
        print(f"The number {number} is negative.")
    else:                                               # number == 0
        print(f"The number {number} is zero.")


sign(int(input()))
