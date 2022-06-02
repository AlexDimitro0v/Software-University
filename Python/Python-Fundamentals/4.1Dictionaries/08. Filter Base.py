def solve():
    # Creating 3 dictionaries and filling them according to the input using try and except
    data = input()
    sep = '=' * 20
    dic_position = dict()
    dic_age = dict()
    dic_salary = dict()
    while data != "filter base":
        personal_info = data.split(" -> ")
        name = personal_info[0]
        information = personal_info[1]

        try:
            information = float(information)  # casting the string info to float so we can check for age and salary
            if information.is_integer():      # if information % 1 == 0.0: or if float(information)-int(information)==0:
                dic_age[name] = int(information)
            else:
                dic_salary[name] = information
        except ValueError:
            dic_position[name] = information

        data = input()

    # print(dic_age)
    # print(dic_salary)
    # print(dic_position)

    string_input = input()

    if string_input == "Age":
        for key, value in dic_age.items():
            print(f"Name: {key}\nAge: {value}")
            print(sep)
    if string_input == "Salary":
        for key, value in dic_salary.items():
            print(f"Name: {key}\nSalary: {value}")
            print(sep)

    if string_input == "Position":
        for key, value in dic_position.items():
            print(f"Name: {key}\nPosition: {value}")
            print(sep)


if __name__ == '__main__':
    solve()
