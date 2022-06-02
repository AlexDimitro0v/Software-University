# Lists inside Dictionary
# https://thispointer.com/python-check-if-a-list-contains-all-the-elements-of-another-list/  all and any functions


def create_main_dic():
    dic = dict()
    data = input()
    while data != 'filter':
        list_topics = data.split(' -> ')
        topic = list_topics[0]
        list_tags = list_topics[1].split(', ')

        if topic not in dic.keys():
            dic[topic] = []

        for tag in list_tags:
            if tag not in dic[topic]:
                dic[topic] += [tag]

        data = input()

    # print(dict)
    return dic


def check_tagging(dic):
    tags = input().split(', ')

    for topic, tag in dic.items():
        if all(elem in dic[topic] for elem in tags):   # Checks if a list contains all the elements of another list
            print(f"{topic} | #{', #'.join(tag)}")


def main():
    dic = create_main_dic()
    check_tagging(dic)


if __name__ == '__main__':
    main()
