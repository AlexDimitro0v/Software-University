def rotate_list(lst):
    # Function to rotate a list by 1 place to the right
    """
    :param   lst:    a list
    :return: no returning value
    """
    last_element = lst.pop(-1)         # cuts the last element and keep it in a variable
    lst.insert(0, last_element)        # inserts the variable in the beginning of the list


def main():
    lst = input("Enter list elements: ").split(' ')  # split returns a list of strings
    rotate_list(lst)
    for item in lst:
        print(item, end=" ")
    print()
    # print(' '.join(lst))


if __name__ == '__main__':
    main()

