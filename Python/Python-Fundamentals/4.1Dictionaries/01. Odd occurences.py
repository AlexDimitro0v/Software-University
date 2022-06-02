def solve(lst):
    # Dictionary Comprehension solution
    counts = {word: lst.count(word) for word in lst}

    occ_list = []

    for key, value in counts.items():
        if value % 2 == 1:
            occ_list.append(key)

    print(*occ_list, sep=', ')


# ______________________________________________________________________________________________
# another way
def count_odd_occurrences1(lst):
    counts = dict()
    for item in lst:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1

    result = ', '.join([str(w) for w in counts if counts[w] % 2 != 0])
    print(result)


# ______________________________________________________________________________________________
# another way
def count_odd_occurrences2(lst):
    counts = dict()

    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    string_output = ""
    for key, value in counts.items():
        if value % 2 == 1:
            string_output += key + ', '
            # print(', '.join(key))  be careful what you joins
    print(string_output.strip(', '), end=' ')  # strip -> removes a char from both sides of a string
    # print()
    # print(' '.join(map(str, counts.values())))
    # print(*counts.items())
    # print(' '.join(counts))    # or counts.keys() - returns a list of all the keys


def main():
    lst = input().lower().split()
    solve(lst)


if __name__ == '__main__':
    main()
