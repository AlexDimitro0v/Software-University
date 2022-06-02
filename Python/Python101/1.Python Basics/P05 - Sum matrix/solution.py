def sum_matrix(m: list):
    try:
        result = 0
        for lst in m:
            result += sum(lst)
        return result
    except:
        raise Exception("Incorrect parameter data type was given to the function.")


if __name__ == '__main__':
    tests = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 45),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
        ([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]], 55)
    ]
    
    for test, expected in tests:
        result = sum_matrix(test)
        print(result == expected)
