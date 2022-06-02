def nan_expand(times: int):
    try:
        times = int(times)
        qualifier = "Not a "
        return (qualifier*times) + "NaN" if times else ""
        
    except:
        raise Exception("Incorrect parameter data type was given to the function.")


def nan_expand_recursive(times: int):
    try:
        times = int(times)
        result = "Not a NaN"
        
        if times == 0:
            return ""
        
        if times == 1:
            return result
        
        while times > 1:
            result = result.replace("NaN", "Not a NaN")
            times -= 1
        
        return result
    
    except:
        raise Exception("Incorrect parameter data type was given to the function.")


if __name__ == '__main__':
    tests = [
        ('2', "Not a Not a NaN"),
        (0, ""),
        (1, "Not a NaN"),
        (2, "Not a Not a NaN"),
        (3, "Not a Not a Not a NaN")
    ]
    
    for test, expected in tests:
        result = nan_expand(test)
        print(result == expected)
