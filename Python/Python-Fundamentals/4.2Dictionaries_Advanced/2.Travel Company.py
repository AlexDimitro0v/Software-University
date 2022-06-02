# Dictionaries inside a dictionary
def create_main_dic():
    dic = dict()
    data = input()
    while data != "ready":
        # getting data for every loop iteration:
        data = data.split(':')
        city = data[0]                               # 1    # Athens (plain text)
        dic_values = data[1].split(',')              # 2    # ['bus-40', 'airplane-300', 'train-150']  (as elements)

        if city not in dic.keys():
            dic[city] = dict()
        for item in dic_values:
            vehicle = item.split('-')[0]             # 3        # bus  airplane train
            capacity = int(item.split('-')[1])       # 4        # 40    300      150

            dic[city][vehicle] = capacity            # overriding allowed

        data = input()

    return dic


def travelling(dic):
    travellers = input()
    while travellers != "travel time!":
        city, people = travellers.split(' ')

        # print(dic[city])         # {'bus': 40, 'airplane': 350, 'train': 150, 'minibus': 8}  the inner dic
        # print(dic[city][item])   # the values of the inner dic --> the available seats
        seats = sum(dic[city].values())
        if int(people) <= seats:
            print(f"{city} -> all {people} accommodated")
        else:
            print(f"{city} -> all except {int(people)-seats} accommodated")

        travellers = input()


def main():
    dic = create_main_dic()
    travelling(dic)          # the printing part


if __name__ == '__main__':
    main()
