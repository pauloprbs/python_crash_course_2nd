import json

def get_stored_username():

    filename = "username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
    
def get_new_username():

    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username
def greet_user():

    username = get_stored_username()
    if username:
        answer = input(f"Your username are {username} (y/n)?")
        if answer == 'y':
            print(f"Welcome back, {username}!")
        elif answer == 'n':
            username = get_new_username()
            print(f"We saved your username, {username}.")
        else:
            print("Invalid answer.")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()