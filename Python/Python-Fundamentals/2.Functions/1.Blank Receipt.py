def header():
    return "CASH RECEIPT \n------------------------------"
    # return is used, so print IS do needed when calling the function


def body():
    print("Charged to____________________ \nReceived by___________________")
    # no need for print when calling the function - example of a void function


def footer():
    print("------------------------------ \n© SoftUni")


def blank_receipt():
    print(header())
    body()
    footer()


blank_receipt()
