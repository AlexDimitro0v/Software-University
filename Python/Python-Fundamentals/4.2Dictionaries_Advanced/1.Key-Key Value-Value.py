# Lists inside Dictionary
def solve():
    key = input().strip()
    value = input().strip()
    n = int(input())
    for times in range(n):
        keys, values = input().split(' => ')
        if key in keys:
            print(f"{keys}:")
            if value in values:
                all_values = '\n'.join([f'-{v}' for v in values.split(';') if value in v])
                print(all_values)


# _____________________________________________________________________________________________________________________
# another way  - poor time performance
def create_main_dic(n):
    dic = dict()
    for times in range(n):
        key, value = input().split(' => ')
        value_list = value.split(';')       # results in a list ex: ['testval', 'x', 'y']
        dic[key] = value_list
    return dic


def main():
    key = input()
    value = input()
    n = int(input())
    dic = create_main_dic(n)
    for k, v in dic.items():
        if key in k:
            print(f"{k}:")
            for item in v:
                if value in item:
                    print(f"-{item}")
# _____________________________________________________________________________________________________________________


if __name__ == '__main__':
    solve()
