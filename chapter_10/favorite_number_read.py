import json

filename = "favorite_number.json"

try:
    with open(filename) as f:
        fav_number = json.load(f)
        print(f"I know your favorite number! It's {fav_number}.")
except FileNotFoundError:
    print("I don't saved your favorite number yet.")