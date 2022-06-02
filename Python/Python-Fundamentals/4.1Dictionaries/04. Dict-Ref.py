def solve1():
    my_dict = dict()
    while True:
        lst = input().split()                # creating a list

        if "end" in lst:
            break
        name = lst[0]
        value = lst[2]

        # In case you are given a name and a second name,
        # you must store the given name with the same value as the value of the second name.
        if value in my_dict.keys():          # If the given second name DOES NOT exist, you must IGNORE that input
            key = value
            my_dict[name] = my_dict[key]     # Accessing value from key ->>> dic[key] = value
        else:
            if value.isdigit():
                my_dict[name] = value        # If the name already EXISTS, you must CHANGE its value with the given one.

    for key, values in my_dict.items():
        print(f"{key} === {int(values)}")


# ____________________________________________________________________________________________________-
# another way
def solve2():
    data = input()
    my_dict = dict()

    while data != "end":
        name, value = data.split(" = ")

        if value.isdigit():             # If the name already EXISTS, you must CHANGE its value with the given one.
            my_dict[name] = value
        elif value in my_dict.keys():
            key = value
            my_dict[name] = my_dict[key]

        data = input()

    for key, value in my_dict.items():
        print(f"{key} === {int(value)}")


if __name__ == '__main__':
    solve1()
