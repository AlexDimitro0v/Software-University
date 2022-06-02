def gas_stations(distance, tank_size, stations):
    try:
        
        return
        
    except:
        raise Exception("Incorrect parameter data type was given to the function.")


if __name__ == '__main__':
    tests = [
        ((320, 90, [50, 80, 140, 180, 220, 290]), [80, 140, 220, 290]),
        ((390, 80, [70, 90, 140, 210, 240, 280, 350]), [70, 140, 210, 280, 350]),
        ((100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]), [40, 80]),
        ((100, 101, [200]), []),
        ((100, 50, [200]), []),
        ((100, 50, [10, 90]), []),
    ]
    
    for distance, tank_size, stations, expected in tests:
        result = gas_stations(distance, tank_size, stations)
        print(result == expected, result)
