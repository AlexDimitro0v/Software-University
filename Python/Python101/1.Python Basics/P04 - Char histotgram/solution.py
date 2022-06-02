def char_histogram(string: str):
    try:
        histogram = {}
        for char in string:
            if char not in histogram:
                histogram[char] = 0
                # histogram[char] = string.count(char)  # count makes additional iteration 0(n^2)
            histogram[char] = histogram[char]+1
        return histogram
    except:
        raise Exception("String data type expected.")


def char_histogram_2(string: str):
    result = {}
    for char in string:
        result[char] = result.get(char, 0) + 1

    return result


def update_dict(dd, char):
    if char not in dd:
        dd[char] = 1
    else:
        dd[char] += 1


def update_dict_2(dd, char):
    if char not in dd:
        dd[char] = 0
    dd[char] += 1


if __name__ == '__main__':
    tests = [
        ("", {}),
        ("    ", {' ': 4}),
        ("Python!", {'P': 1, 'y': 1, 't': 1, 'h': 1, 'o': 1, 'n': 1, '!': 1}),
        ("AAAAaaa!!!", {'A': 4, 'a': 3, '!': 3}),
        ("Some very long string here with different casing", {
            'S': 1,
            'o': 2,
            'm': 1,
            'e': 6,
            ' ': 7,
            'v': 1,
            'r': 4,
            'y': 1,
            'l': 1,
            'n': 4,
            'g': 3,
            's': 2,
            't': 3,
            'i': 4,
            'h': 2,
            'w': 1,
            'd': 1,
            'f': 2,
            'c': 1,
            'a': 1
        })
    ]
    
    for test, expected in tests:
        result = char_histogram(test)
        print(result == expected)
