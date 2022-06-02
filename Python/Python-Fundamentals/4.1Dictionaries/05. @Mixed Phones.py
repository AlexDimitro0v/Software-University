# https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/   sorting dictionaries in Python
def solve1():
    my_dict = dict()

    while True:
        phones = input().split(' : ')
        if "Over" in phones:
            break
        if phones[1].isdigit():
            my_dict[phones[0]] = phones[1]
        else:
            my_dict[phones[1]] = phones[0]

    sorted_dict = sorted(my_dict.keys())        # sorts a dictionary by the keys
    for key in sorted_dict:                     # or just for key in sorted(my_dict):
        print(f"{key} -> {my_dict[key]}")


def solve2():
    my_dict = dict()
    data = input()
    while data != 'Over':
        data = data.split(' : ')
        name = data[0]
        tel_number = data[1]
        if name.isdigit():              # IF the string is digit...could also be rewritten with try, except
            my_dict[tel_number] = name
        else:
            my_dict[name] = tel_number
        data = input()

    # my_dict = dict(sorted(my_dict.items(), key=lambda kvp: kvp[0]))
    for key, value in sorted(my_dict.items()):
        print(f"{key} -> {value}")


if __name__ == '__main__':
    # print(help(sorted))
    # print(help(list.sort))
    solve2()
