def count_letter_occurrences(string):
    count = dict()
    for letter in string:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for key, value in count.items():
        print(f"{key} -> {value}")


def main():
    string = input()
    count_letter_occurrences(string)


if __name__ == '__main__':
    main()
