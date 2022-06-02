import math
# Lists inside Dictionary


def solve():
    shellbound = dict()

    shell = input()
    while shell != 'Aggregate':
        list_place_and_size = shell.split()
        region = list_place_and_size[0]
        size = int(list_place_and_size[1])
        if region not in shellbound:
            shellbound[region] = []
        if size not in shellbound[region]:
            shellbound[region].append(size)
        shell = input()
        # print(shellbound[region])       -> [50, 20, 30]
        # print(shellbound.values())      -> dict_values([[50, 50, 20, 30], [10, 20]])

    for key, value in shellbound.items():
        giant_shell = math.ceil(sum(value) - sum(value) / len(value))
        print(f"{key} -> {', '.join(map(str,value))} ({giant_shell})")


if __name__ == '__main__':
    solve()
