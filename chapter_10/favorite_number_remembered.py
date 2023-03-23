import json

filename = "favorite_number.json"

try:
    with open(filename) as f:
        fav_number = json.load(f)
        print(f"I know your favorite number! It's {fav_number}.")
except FileNotFoundError:
    fav_number = input("Enter your favorite number: ")

    try:
        fav_number = int(fav_number)
    except ValueError:
        print("This is not a number.")
    else:
        filename = "favorite_number.json"
        with open(filename, 'w') as f:
            json.dump(fav_number, f)
        print("Your favorite number are saved.")