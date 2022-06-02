# LEGB (the scope resolution) stands for Local->Enclosed->Global->Built-In
# https://www.youtube.com/watch?v=QVdf0LgmICw
# https://stackoverflow.com/questions/18864041/why-can-functions-in-python-print-variables-in-enclosing-scope-but-cannot-use-th
# https://www.geeksforgeeks.org/scope-resolution-in-python-legb-rule/


def fun():
    string = 'hello'

    def nested_fun():
        global string
        string = 'hiya'

    print("Before calling nested_fun: " + string)
    nested_fun()
    print("After calling nested_fun: " + string)       # 'hello'


string = 'hola'
fun()
print("str in main module: " + string)                 # ' hiya'


print('-------------------------------')


def fun():
    global stri
    print(stri)
    stri = 'hiya'


stri = 'hello World'
fun()
print(stri)

print('--------------------------------')


# ____________________wild combination of local and global var ________________________
def foo(x, y):
    global a
    a = 42
    x, y = y, x
    b = 33
    b = 17
    c = 100
    print(a, b, x, y)


a1, b1, x1, y1 = 1, 15, 3, 4
foo(17, 4)
print(a1, b1, x1, y1)


# __________________________________________________________Global Variables in Nested Functions
variable = 0


def f():
    variable = 42

    def g():
        global variable
        variable = 43
    print("Before calling g: " + str(variable))     # 42
    print("Calling g now:")                         # Calling g now
    g()
    print("After calling g: " + str(variable))      # 42 the global keyword in nested functions does not affect the
                                                    # namespace of their enclosing namespace!


f()
print("The variable in main: " + str(variable))     # 43
# Using globals should be a must - they should be avoided as using globals may seem convenient at first.
# But the practice can make the code hard to debug and organize into modules.
