"""
Write a program that reads the user first name, last name, age and current town.
Then print the taken information in the form:
"You are {firstName} {lastName}, a {age}-years old person from {town}".
"""


def person_presentation(f_name, l_name, age, place):
    print("You are %s %s, a %d-years old person from %s." % (f_name, l_name, age, place), end='')


first_name = input("Enter your forename: ")
last_name = input("Enter your family name: ")
user_age = int(input("Enter your age: "))
town = input("Enter your town: ")
person_presentation(first_name, last_name, user_age, town)
print(" Same line")                                         # end='' is a common practice - it leaves the cursor on the
#                                                           same line
