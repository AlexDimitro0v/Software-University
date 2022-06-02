"""
Input:
• Age (integer)
• Gender (string)

Output:
Display title according to the input.
"Mr." if gender == 'm' and age >= 16
"Master" if gender == 'm' and age < 16
"Ms." if gender == 'f' and age >=16
"Miss" if gender == 'f' and age < 16
"""


def display_title(age, gender):
    if gender == "f":
        if age >= 16:
            print("Ms.")
        elif age < 16:
            print("Miss")
    elif gender == "m":
        if age >= 16:
            print("Mr.")
        elif age < 16:
            print("Master")


def main():
    age = float(input("Enter age: "))
    gender = input("Enter gender: ")
    display_title(age, gender)


if __name__ == '__main__':
    main()
