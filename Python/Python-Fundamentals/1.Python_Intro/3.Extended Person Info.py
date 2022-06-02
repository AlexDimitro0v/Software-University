def display_person_info(name, age, town, salary):
    age_range = None     # Good practice: initializing a variable
    salary_range = None  # However here this is not needed because we have checked every case (if elif else)

    if age < 18:
        age_range = "teen"
    elif age < 70:       # if age in range(18,70)    # because it asks everytime it sees 'if'
        age_range = "adult"
    else:
        age_range = "elder"

    if salary < 500:
        salary_range = "low"
    elif salary < 2000:   # if 500 <= salary < 2000:
        salary_range = "medium"
    else:
        salary_range = "high"

    salary = f"{salary:.2f}"

    print(f" \n\
    Name: {name}\n\
    Age: {age}\n\
    Town: {town}\n\
    Salary: ${salary}\n\
    Age range: {age_range}\n\
    Salary range: {salary_range}\
    ")

    # \n for a new line


def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    town = input("Enter your town: ")
    salary = float(input("Enter your salary: "))
    display_person_info(name, age, town, salary)


if __name__ == '__main__':
    main()
