"""
Write a program the calculates the ASCII values of several names and finds the winner, the name with the greatest value
is the winner. You will read names from the console until you get the command 'STOP'. Finally, write:
• "Winner is {the winner} - {the total ASCII value of the characters his name consists of}!"
"""


def solve():
    name = input()
    max_so_far = 0
    winner = None

    while name != 'STOP':
        total = 0
        for letter in name:
            total += ord(letter)

        if total > max_so_far:
            max_so_far = total
            winner = name
        name = input()

    return f"Winner is {winner} - {max_so_far}!"


if __name__ == '__main__':
    print(solve())
