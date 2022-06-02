# Void function (does not return a value)
def add(num1, num2):
    print("Sum is", num1 + num2)


try:
    result = add(10, 200) + int(100)
    print(result)
except TypeError:
    print("You can't play with void functions")


# ______________________________________________________
# Returning function
def add(num1, num2):
    return num1 + num2


result = add(10, 190) + 300

print(result)

# Conclusion: You can't play with void functions
