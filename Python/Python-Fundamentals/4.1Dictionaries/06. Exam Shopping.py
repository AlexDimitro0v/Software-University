def solve():
    my_dict = dict()

    while True:
        products = input().split()
        if "shopping" and 'time' in products:
            break
        stock_product = products[1]
        stock_quantity = int(products[2])          # casting the dic value to int, so we can add it
        if stock_product in my_dict.keys():
            my_dict[stock_product] += stock_quantity
        else:
            my_dict[stock_product] = stock_quantity

    # Buying part
    buying = input()
    while not buying == "exam time":
        buy_list = buying.split()
        buy_product = buy_list[1]
        buy_quantity = int(buy_list[2])
        if buy_product not in my_dict.keys():
            print(f"{buy_product} doesn't exist")
        elif my_dict[buy_product] <= 0:
            print(f"{buy_product} out of stock")
        else:
            my_dict[buy_product] -= buy_quantity

        buying = input()

    # print(dict)
    for key, value in my_dict.items():
        if value > 0:
            print(f"{key} -> {value}")


if __name__ == '__main__':
    solve()
