def display_person_info(name, age, town, salary):
    print(f"{name} is {age} years old, is from {town} and makes ${salary}")


def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    town = input("Enter your town: ")
    salary = float(input("Aaaand enter your salary: "))
    display_person_info(name, age, town, salary)


if __name__ == '__main__':
    main()
