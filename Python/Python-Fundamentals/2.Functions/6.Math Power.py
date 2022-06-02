# Reading user input every time a function is invoked.
def power_f():
    number = float(input())
    power = int(input())
    return number ** power


print(power_f())
