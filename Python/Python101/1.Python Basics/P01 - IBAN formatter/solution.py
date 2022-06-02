def iban_formatter(iban: str):
    try:
        iban = iban.replace(' ', '')
        container = []
        temp = ""
        for symbol in iban:
            temp += symbol
            if len(temp) == 4:
                container.append(temp)
                temp = ""

        container.append(temp)
        return ' '.join(container)

    except:
        raise Exception("An incorrect IBAN number was provided.")


if __name__ == '__main__':
    tests = [
        ("BG80BNBG96611020345678", "BG80 BNBG 9661 1020 3456 78"),
        ("BG80 BNBG 9661 1020 3456 78", "BG80 BNBG 9661 1020 3456 78"),
        ("BG14TTBB94005362446381", "BG14 TTBB 9400 5362 4463 81"),
        ("BG14 TTBB 9400 5362 4463 81", "BG14 TTBB 9400 5362 4463 81"),
        ("BG91UNCR70001864961754", "BG91 UNCR 7000 1864 9617 54"),
        ("BG91 UNCR 7000 1864 9617 54", "BG91 UNCR 7000 1864 9617 54")
    ]

    for iban, expected in tests:
        result = iban_formatter(iban)
        # print(f"'{expected}', '{result}'")
        print(result == expected)
