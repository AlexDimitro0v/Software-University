"""
Write a console program that reads a password (one line with a random text string) and checks if the input match
“s3cr3t!P@ssw0rd”. If the two passwords match - output "Welcome", otherwise - “Wrong password!”.
"""
# Algorithm
# 1. Read input string
# 2. Compare input with "s3cr3t!P@ssw0rd"
#   a: match - > print(Welcome)
#   b: not -> print(Wrong password!)


def correct_pass(passwd):
    if passwd == "s3cr3t!P@ssw0rd":
        return True
    return False


if __name__ == '__main__':
    password = input("Give me a password: ")
    if correct_pass(password):
        print("Welcome")
    else:
        print("Wrong password!")
