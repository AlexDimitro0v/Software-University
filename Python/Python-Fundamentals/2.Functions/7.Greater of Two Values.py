def greater_value(data_type, arg1, arg2):
    if data_type == 'int':
        if arg1 > arg2:
            return arg1
        else:
            return arg2
    elif data_type == 'string':
        if str(arg1) > str(arg2):
            return arg1
        else:
            return arg2
    elif data_type == 'char':
        if ord(arg1) > ord(arg2):
            return arg1
        else:
            return arg2
    else:
        return 'Not supported data type'


def main():
    data_type = input()
    if data_type == 'int':
        arg1 = int(input())
        arg2 = int(input())
    else:
        arg1 = input()
        arg2 = input()

    print(greater_value(data_type, arg1, arg2))


if __name__ == "__main__":
    main()
