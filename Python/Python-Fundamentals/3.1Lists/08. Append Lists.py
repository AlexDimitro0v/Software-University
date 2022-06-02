def solve(data):
    # data.reverse()

    result = []
    for item in reversed(data):
        temp_list = item.split()
        temp_list = list(filter(None, temp_list))     # possible edge-case
        result.extend(temp_list)
        # result += item

        # The extend() extends the list by adding all items of a list (passed as an argument) to the end.

    print(" ".join(result))


def main():
    data = input().split("|")
    solve(data)


if __name__ == '__main__':
    main()
