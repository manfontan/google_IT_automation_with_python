def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")
attempts(5)

def get_username():
    return input("Enter username: ")

def valid_username(username):
    return len(username) > 3

username = get_username()

while not valid_username(username):
    print("Invalid username")
    username = get_username()
