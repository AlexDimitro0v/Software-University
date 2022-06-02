def solve1():
    dict_data = dict()
    user = input()
    while user != "login":
        lst = user.split(" -> ")
        username = lst[0]
        password = lst[1]
        dict_data[username] = password    # storing the data into the database
        user = input()

    # print(dict_data)  # printing is always useful for debugging!!!

    # dict_user_password = dict()
    requests = input()
    count = 0
    while not requests == "end":
        login = requests.split(' -> ')
        username = login[0]
        password = login[1]
        if username not in dict_data.keys():
            # dict_user_password[username] = "login failed"
            result = f"{username}: login failed"
            count += 1
        else:
            if password == dict_data[username]:
                # dict_user_password[username] = "logged in successfully"
                result = f"{username}: logged in successfully"
            else:
                # dict_user_password[username] = "login failed"
                result = f"{username}: login failed"
                count += 1

        requests = input()
        print(result)

    print(f"unsuccessful login attempts: {count}")


def solve2():
    users = {}

    line = input()
    while line != 'login':
        username, password = filter(None, line.split(' -> '))
        users[username] = password
        line = input()

    result = ''
    attempts = 0

    line = input()
    while line != 'end':
        username, password = filter(None, line.split(' -> '))
        if username in users and users[username] == password:
            result += f'{username}: logged in successfully\n'
        else:
            result += f'{username}: login failed\n'
            attempts += 1

        line = input()

    result += f'unsuccessful login attempts: {attempts}\n'
    print(result)


if __name__ == '__main__':
    solve1()
